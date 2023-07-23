from django.shortcuts import render,HttpResponse
from django.views import View
# Create your views here.
class Home(View):
    def get(self, request):
        return render(request,"public/home.html")
