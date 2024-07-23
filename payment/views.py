from django.shortcuts import redirect, get_object_or_404, reverse
from orders.models import Order
import requests
import json
from django.conf import settings
from django.http import HttpResponse


def payment_process(request):
    # Get the saved order_id from session.
    order_id = request.session.get('order_id')
    # Get the Order object from order-id
    order = get_object_or_404(Order, id=order_id)
    toman_total_price = order.total_order_price()
    rial_total_price = toman_total_price * 10

    zarinpal_request_url = 'https://api.zarinpal.com/pg/v4/payment/request.json'
    # data and header of the request that we should post to the url above
    request_header = {
        'accept': 'application/json',
        'content-type': 'application/json'
    }

    request_data = {
        'merchant_id': settings.DJANGO_ZARINPAL_MERCHANT_ID,
        'amount': rial_total_price,
        'description': f'#{order_id}:{order.user.first_name} {order.user.last_name}',
        'callback_url': request.build_absolute_uri(reverse('payment:callback')),

    }
    res = requests.post(url=zarinpal_request_url, data=json.dumps(request_data), headers=request_header)

    response_data = res.json()['data']  # get the response data from zarinpal and save it as a dict in python
    authority = response_data['authority']  # save the response authority in a variable and
    order.authority = authority  # match it with order authority in database
    order.save()  # and then save it on database

    if 'errors' not in response_data or len(request_data['errors']) == 0:
        return redirect(f'https://www.zarinpal.com/pg/StartPay/{authority}'.format(authority=authority))
    else:
        return HttpResponse('error')


def payment_callback(request):
    payment_authority = request.GET.get('Authority')
    payment_status = request.GET.get('status')
    order = get_object_or_404(Order, zarinpal_authority=payment_authority)
    toman_total_price = order.total_order_price()
    rial_total_price = toman_total_price * 10
    zarinpal_verify_url = 'https://api.zarinpal.com/pg/v4/payment/verify.json'

    if payment_status == 'OK':
        request_header = {
            'accept': 'application/json',
            'content-type': 'application/json'
        }

        request_data = {
            'merchant_id': settings.DJANGO_ZARINPAL_MERCHANT_ID,
            'amount': rial_total_price,
            'authority': payment_authority,
        }
        res = requests.post(url=zarinpal_verify_url, data=json.dumps(request_data), headers=request_header)
        response_data = res.json()['data']
        if 'errors' not in response_data or len(request_data['errors']) == 0:
            payment_code = response_data['code']

            if payment_code == 100:
                order.is_paid = True
                order.zarinpal_ref_id = response_data['ref_id']
                order.zarinpal_verify_data = response_data
                order.save()
                return HttpResponse('پرداخت با موفقیت انجام شد.')
            elif payment_code == 101:
                return HttpResponse('این پرداخت قبلا با موفقیت انجام شده است.')

            else:
                error_code = res.json()['errors']['code']
                error_message = res.json()['errors']['message']
                return HttpResponse(f'تراکنش ناموفق بود. {error_code} {error_message}')
    else:
        return HttpResponse('تراکنش ناموفق بود.')