from django.contrib import messages
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from home.models import Contact

# Create your views here.
def index(request):
    return render(request,'index.html')

def project(request):
    return render(request,'project.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phn= request.POST.get('phn')
        desc= request.POST.get('desc')
        contact = Contact(name=name, email=email, phn=phn, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request,'index.html')
