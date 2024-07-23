from django.urls import path
from .views import HomePageView, contactus, profile

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contactus/', contactus, name='contactus' ),
    path('myprofile/', profile, name='my_profile')
]
