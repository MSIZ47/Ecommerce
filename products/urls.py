from django.urls import path, include
from .views import ProductListView, ProductDetailView, CommentCreateView


urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('comments/<int:product_id>/', CommentCreateView.as_view(), name='product_comments'),

]