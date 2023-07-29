from django.urls import path
from .views import *
urlpatterns = [
    path('',Home.as_view(),name="home"),
    path('about',About.as_view(),name="about"),
    path('contact',Contact.as_view(),name="contact"),
    path('login',Login.as_view(),name="login"),
    path('signup',Signup.as_view(),name="signup"),
    path('logout',LogOut.as_view(),name="logout"),
    path('forgot-password',ForgetPassword.as_view(),name="forget-password"),
    path('reset-password',ResetPassword.as_view(),name="reset-password"),
    path('cart',Cart.as_view(),name="cart"),
    path('dashboard',Dashboard.as_view(),name="dashboard"),
]
