from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from passlib.hash import django_pbkdf2_sha256 as handler
import openai
from django.http import JsonResponse
import os
import requests
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
import random
from django.contrib import messages
from .models import *
from django.core.files.base import ContentFile
from .helper import login_required
from django.utils.decorators import method_decorator

openai.api_key ="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"

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
        if request.session['login']:
            return redirect("/dashboard")
        return render(request,"public/login.html")
    def post(self, request):
         email=request.POST['email']
         password=request.POST['password']
         user=UserModel.objects.filter(email=email)
         if user:
            if user[0].is_email_verified==True:
                if handler.verify(password,user[0].password):
                    request.session["login"] =True
                    request.session["pk"] =user[0].pk
                    request.session["email"] =user[0].email
                    messages.success(request,"Successfully Login")
                    user[0].is_active=True
                    user[0].save()
                    return redirect("/dashboard")
                else:
                    messages.error(request,"please enter email and password")
                    return redirect("/login")
            else:
                messages.error(request,"please Verify Your Account")
                return redirect("/login")            
         else:
                messages.error(request,"please Create Your Account")
                return redirect("/login")  

class Signup(View):
    def get(self, request):
       
        return render(request,"public/signup.html")
    def post(self, request):
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST['email']
        password = handler.hash(request.POST["password"])
        token=random.randint(1000, 9999)
        addData= UserModel(first_name=first_name, last_name=last_name, email=email, password=password,email_verification_token=token)
        addData.save()
        userInfo={
            "id": addData.pk,
            "name": f"{addData.first_name} {addData.last_name}",
            "token": addData.email_verification_token
        }
        html_template = 'email/verification.html'
        html_message = render_to_string(html_template, context=userInfo)
        subject = "Please Verify Your Account"
        email_from ="info@developerwings.com"
        recipient_list = [addData.email]

        message = EmailMessage(subject, html_message, email_from, recipient_list)
        message.content_subtype = 'html'
        message.send()
        return render(request, 'public/signup-verify-message.html')


class VerifyAccount(View):
    def get(self,request,id,token):
        verify=UserModel.objects.get(pk=id,email_verification_token=token)
        if verify:
            verify.is_email_verified=True
            verify.email_verification_token=""
            verify.save()
        messages.success(request,"Your account has been verified successfully")
        return redirect("/login")

class ForgetPassword(View):
    def get(self, request):
       
        return render(request,"public/forget-password.html")
    
    def post(self, request):
        email=request.POST.get('email')
        user=UserModel.objects.get(email=email)
        user.email_verification_token=random.randint(1000, 9999)
        user.save()
        userInfo={
            "id": user.pk,
            "name": f"{user.first_name} {user.last_name}",
            "token": user.email_verification_token
        }
        html_template = 'email/forget-password.html'
        html_message = render_to_string(html_template, context=userInfo)
        subject = "Please Reset Your Account Password"
        email_from ="info@developerwings.com"
        recipient_list = [user.email]

        message = EmailMessage(subject, html_message, email_from, recipient_list)
        message.content_subtype = 'html'
        message.send()
        messages.success(request,"Reset Password Link Sent to your email address")
        return redirect('/login')

 
class ResetPassword(View):
    def get(self, request):
       
        return render(request,"public/reset-password.html")
 

class LogOut(View):
    def get(self, request):
        if request.session.has_key('login') and request.session.has_key('pk'):
            user=UserModel.objects.get(pk=request.session['pk'])
            user.is_active=False
            user.save()
            del request.session['login']
            del request.session["pk"] 
            del request.session["email"]
            messages.success(request,"Successfully Log Out")
        
            return redirect("/login")
        
class ResetPassword(View):
    def get(self, request,id,token):
       return render(request, "public/password-reset.html",{'id':id,'token':token})
    
    def post(self, request,id,token):
        user=UserModel.objects.get(pk=id,email_verification_token=token)
        if user:
            user.password=handler.hash(request.POST.get('password'))
            user.email_verification_token=""
            user.save()
            messages.success(request,"your password has been reset successfully")
            return redirect('/login')
        else:
            messages.success(request,"your Token has been expired")
            return redirect('/login')

    
class Cart(View):
    def get(self, request):
        return render(request, 'public/cart.html')
    

@method_decorator(login_required, name='dispatch')
class Dashboard(View):
    def get(self, request):
        return render(request, 'public/dashboard.html')

class Profile(View):
    def get(self, request):
        data= UserModel.objects.get(pk=request.session['pk'])
      
        return render(request, 'public/profile.html',{"data":data})

class EditProfile(View):
    def get(self, request):
        return render(request, 'public/edit-profile.html')


class SavedAddress(View):
    def get(self, request):
        return render(request, 'public/saved-address.html')

class Wishlist(View):
    def get(self, request):
        data= SaveToFavoriteModel.objects.filter(user=request.session['pk'])
        print(data)
        return render(request, 'public/wishlist.html',{'data':data})

class DeleteWishlist(View):
    def get(self, request,id):
        print(id)
        data= SaveToFavoriteModel.objects.get(user=request.session['pk'],pk=id)
        data.delete()

        messages.success(request,"Wishlist deleted Successfully")
        return redirect('/whishlist')

class Orders(View):
    def get(self, request):
        return render(request, 'public/order.html')
    

class Products(View):
    def get(self, request):
        search=request.GET.get('search')
        response = openai.Image.create(
        prompt=search,
        
        n=6,
        size="512x512"
        )
        print(response['data'])
        image_url = response['data'][0]['url']
        print(image_url)
        
    
        return render(request, 'public/product.html',{"data":response['data']})

class SingleProduct(View):
    def get(self, request):
        return render(request, 'public/single-product.html')

class CheckOut(View):
    def get(self, request):
        return render(request, 'public/checkout.html')
    

        

class SaveToFavorite(View):
    def get(self, request):
     try:
        # Download the file from the URL
        url= request.GET.get('image')
        response = requests.get(url)
        print(response)
        if response.status_code == 200:
            user= UserModel.objects.get(pk=request.session["pk"])
            image = SaveToFavoriteModel(user=user)

            # Set the image file data
            image.image_file.save(os.path.basename(url+".png"), ContentFile(response.content))
            image.save()
            return JsonResponse({
                "message": "Image saved successfully",
                "status": True,
            })

     except Exception as e:
         print(f"Error downloading and storing file: {e}")

    # Handle errors or invalid requests
     return HttpResponse('error_page') 