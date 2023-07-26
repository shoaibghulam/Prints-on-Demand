from django.urls import path
from .views import *
urlpatterns = [
    path('',Home.as_view(),name="home"),
    path('about',About.as_view(),name="about"),
    path('contact',Contact.as_view(),name="contact"),
    path('faq',Faq.as_view(),name="faq"),
    path('login',Login.as_view(),name="login"),
    path('signup',Signup.as_view(),name="signup "),
]
