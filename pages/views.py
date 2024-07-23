from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import ContactUsForm
from accounts.models import CustomUser

class HomePageView(TemplateView):
    template_name = 'home.html'      


def contactus(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            form = ContactUsForm()
            return redirect('contactus')
    else:
        form = ContactUsForm()
    return render(request , 'pages/contact_us.html',context={'form':form})


def profile(request):
    id = request.user.id
    user = CustomUser.objects.filter(pk=id)[0]
    return render(request, 'pages/my_profile.html', {'user':user})

