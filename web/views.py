from django.shortcuts import render,HttpResponse,redirect
from django.views import View
# Create your views here.
class Home(View):
    def get(self, request):
        return render(request,"public/home.html")

class About(View):
    def get(self, request):
        return render(request,"public/about.html")


class Contact(View):
    def get(self, request):
        return render(request,"public/contact.html")


class Login(View):
    def get(self, request):
       
        return render(request,"public/login.html")
    def post(self, request):
         request.session["login"] =True
         return redirect("/")


class Signup(View):
    def get(self, request):
        return render(request,"public/signup.html")


class ForgetPassword(View):
    def get(self, request):
       
        return render(request,"public/forget-password.html")
 
class ResetPassword(View):
    def get(self, request):
       
        return render(request,"public/reset-password.html")
 

class LogOut(View):
    def get(self, request):
        if request.session.has_key('login'):
            del request.session['login']
            return redirect("/")
        

class Cart(View):
    def get(self, request):
        return render(request, 'public/cart.html')

class Dashboard(View):
    def get(self, request):
        return render(request, 'public/dashboard.html')

class Profile(View):
    def get(self, request):
        return render(request, 'public/profile.html')

class EditProfile(View):
    def get(self, request):
        return render(request, 'public/edit-profile.html')


class SavedAddress(View):
    def get(self, request):
        return render(request, 'public/saved-address.html')

class Wishlist(View):
    def get(self, request):
        return render(request, 'public/wishlist.html')