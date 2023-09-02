from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from passlib.hash import django_pbkdf2_sha256 as handler
import openai
from django.http import JsonResponse
import os
import requests
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .mail import sendEmail
import random
from django.contrib import messages
from .models import *
from django.core.files.base import ContentFile
from PIL import Image
import io

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
                    messages.success(request,"Successfully Login")
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
        data=sendEmail("shoaibghulam@gmail.com")
        print(data)
        return render(request,"public/signup.html")
    def post(self, request):
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST['email']
        password = handler.hash(request.POST["password"])
        token=random.randint(1000, 9999)
        addData= UserModel(first_name=first_name, last_name=last_name, email=email, password=password,email_verification_token=token)
        addData.save()
        print(request.POST)
        return render(request, 'public/signup-verify-message.html')


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

class Orders(View):
    def get(self, request):
        return render(request, 'public/order.html')
    

class Products(View):
    def get(self, request):
        search=request.GET.get('search')
        response = openai.Image.create(
        prompt=search,
        
        n=6,
        size="1024x1024"
        )
        print(response['data'])
        image_url = response['data'][0]['url']
        print(image_url)
        
        print(search)
        data=[{
  "url": "https://oaidalleapiprodscus.blob.core.windows.net/private/org-snt5tbcGuQHSaVtFOiWdWDJb/user-hloT6COcAsLpSEjtiOwZb9xY/img-f2vgjiPQQJs3yBsXGyorox3p.png?st=2023-09-01T21%3A33%3A49Z&se=2023-09-01T23%3A33%3A49Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-09-01T06%3A08%3A25Z&ske=2023-09-02T06%3A08%3A25Z&sks=b&skv=2021-08-06&sig=Op/2YzpSW3Pmx4y8yjmE9cnOlMCOHAazlZYKvVkK4Ho%3D"
}, {
  "url": "https://oaidalleapiprodscus.blob.core.windows.net/private/org-snt5tbcGuQHSaVtFOiWdWDJb/user-hloT6COcAsLpSEjtiOwZb9xY/img-1w2PJ5GaD0SFULMYavSx0U0H.png?st=2023-09-01T21%3A33%3A49Z&se=2023-09-01T23%3A33%3A49Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-09-01T06%3A08%3A25Z&ske=2023-09-02T06%3A08%3A25Z&sks=b&skv=2021-08-06&sig=QBxjAJQGgN5p3POs4LROu0oR6/EqN9A7DUaJx/c9v9I%3D"
}, {
  "url": "https://oaidalleapiprodscus.blob.core.windows.net/private/org-snt5tbcGuQHSaVtFOiWdWDJb/user-hloT6COcAsLpSEjtiOwZb9xY/img-Zug156LBAFoLjdcVHdEq3Nrt.png?st=2023-09-01T21%3A33%3A48Z&se=2023-09-01T23%3A33%3A48Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-09-01T06%3A08%3A25Z&ske=2023-09-02T06%3A08%3A25Z&sks=b&skv=2021-08-06&sig=nQNqi/JqmyD9fjrnChs1PbFK0LvLK67I7sU9OP6xVt0%3D"
},{
  "url": "https://oaidalleapiprodscus.blob.core.windows.net/private/org-snt5tbcGuQHSaVtFOiWdWDJb/user-hloT6COcAsLpSEjtiOwZb9xY/img-LP4EaZbHo45mVgcyJE4Sq4QC.png?st=2023-09-01T21%3A33%3A49Z&se=2023-09-01T23%3A33%3A49Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-09-01T06%3A08%3A25Z&ske=2023-09-02T06%3A08%3A25Z&sks=b&skv=2021-08-06&sig=T9cr04oO%2BksmUMiAIURar2iNhh3RfiZ4WW39avjoHVY%3D"
}, {
  "url": "https://oaidalleapiprodscus.blob.core.windows.net/private/org-snt5tbcGuQHSaVtFOiWdWDJb/user-hloT6COcAsLpSEjtiOwZb9xY/img-uhCC2nDGPGoordUg17n9cyWj.png?st=2023-09-01T21%3A33%3A49Z&se=2023-09-01T23%3A33%3A49Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-09-01T06%3A08%3A25Z&ske=2023-09-02T06%3A08%3A25Z&sks=b&skv=2021-08-06&sig=nwL42xIEIM0quSYqkD2XOqXXX/N%2BwAs79S7Yo2ap6FY%3D"
},{
  "url": "https://oaidalleapiprodscus.blob.core.windows.net/private/org-snt5tbcGuQHSaVtFOiWdWDJb/user-hloT6COcAsLpSEjtiOwZb9xY/img-lzfobAMyIPc72vQ95Yt6GiQM.png?st=2023-09-01T21%3A33%3A48Z&se=2023-09-01T23%3A33%3A48Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-09-01T06%3A08%3A25Z&ske=2023-09-02T06%3A08%3A25Z&sks=b&skv=2021-08-06&sig=wsbVDRbPPIIn4MoSLebem/gPdfbRwSNcXtnTSPJF4nM%3D"
}]
        # return render(request, 'public/product.html',{"data":data})
        return render(request, 'public/product.html',{"data":response['data']})

class SingleProduct(View):
    def get(self, request):
        return render(request, 'public/single-product.html')

class CheckOut(View):
    def get(self, request):
        return render(request, 'public/checkout.html')
    

        

class SaveToFavorite(View):
    def get(self, request):
    #  try:
        # Download the file from the URL
        url= request.GET.get('image')
        print(url)
        response = requests.get(url)
        image_content = response.content

        # Use Pillow to open and convert the image to PNG
        image = Image.open(io.BytesIO(image_content))
        image = image.convert("RGBA")

        # Save the converted image as bytes
        with io.BytesIO() as output:
            image.save(output, format="PNG")
            png_content = output.getvalue()

        if response.status_code == 200:
            user= UserModel.objects.get(pk=request.session["pk"])
            saveimg = SaveToFavoriteModel(user=user)

            # Set the image file data
            saveimg.image_file.save(os.path.basename(url+".png"), ContentFile(png_content), save=True)
            saveimg.save()
            return HttpResponse("Hello, world!")

    #  except Exception as e:
        #  print(f"Error downloading and storing file: {e}")

    # Handle errors or invalid requests
        return HttpResponse('error_page') 