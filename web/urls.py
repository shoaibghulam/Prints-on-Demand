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
    path('profile',Profile.as_view(),name="profile"),
    path('edit-profile',EditProfile.as_view(),name="edit-profile"),
    path('saved-address',SavedAddress.as_view(),name="saved-address"),
    path('whishlist',Wishlist.as_view(),name="whishlist"),
    path('orders',Orders.as_view(),name="orders"),
    path('products',Products.as_view(),name="products"),
    path('single-product',SingleProduct.as_view(),name="single-product"),
    path('checkout',CheckOut.as_view(),name="checkout"),
]
