from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    conext={
        'variable':"sent"
    }
    return render(request,'index.html')
    #return HttpResponse("HOME")

def about(request):
    #return HttpResponse("ABOUT")
    return render(request,'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name = name , email=email, phone=phone,desc=desc,date = datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent.")
    return render(request,'contact.html')

def buy(request):
    #return HttpResponse("BUY")
    return render(request,'buy.html')

def ship(request):
    return render(request,'ship.html')

