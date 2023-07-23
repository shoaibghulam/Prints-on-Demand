from django.shortcuts import render,HttpResponse
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


class Faq(View):
    def get(self, request):
        return render(request,"public/faq.html")
