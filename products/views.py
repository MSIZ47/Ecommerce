from django.views.generic import ListView, DetailView, CreateView
from .models import Product, Comment
from .forms import CommentForm
from django.shortcuts import get_object_or_404


class ProductListView(ListView):
    queryset = Product.objects.filter(is_active=True)
    template_name = 'products/index.html'
    context_object_name = 'products'
    paginate_by = 8


class ProductDetailView(DetailView):
    def get_queryset(self):
        return Product.objects.filter(pk=self.kwargs['pk'])

    template_name = 'products/product_details.html'
    context_object_name = 'product'

# we need to send a form as a context to our 'product_detail' template so that user use this form to submit a comment
# for sending context to template we need to overwrite 'get_context_data' and put a context in this function and this
# function will do the rest of the work, so we first create our comment_form class  in 'forms.py' and then we create a
# context from it and then return it

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentForm()  # remember 'comment_form' is the name that we use in our template
        # not 'form'.(comment_form|crispy)
        return context


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm

# we overwrite form_valid function in classed_based_views to handle Comments. first we create a obj from our form_class,
# but don't commit it to database, so we can assign the 'user' and 'product' of our comment. we assign the user with
# self.request.user. but for product we need to use the action of a form in 'product_detail' template to send the id of
# the product that the user wants to comment on it then we get it with 'self.kwargs'  and save it into  a variable
# and assign the product of our comment with 'get_object_or_404' and  give the variable as pk.so at the end after we set
# all the attributes of  our Comment model('datetime filled automatically','text and stars' filled by user and product
# and user handled by us

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user

        product_id = int(self.kwargs['product_id'])
        product = get_object_or_404(Product, id=product_id)
        obj.product = product
        return super().form_valid(form)
