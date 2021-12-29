from django.http.response import HttpResponseGone
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'variable': 'This is sent'
    }
    # return HttpResponseGone("This is homepage")
    
    return render(request, "index.html",context)

def about(request):
    return render(request, "about.html")
    # return HttpResponseGone("This is about page")

def services(request):
    return render(request, "services.html")
    # return HttpResponseGone("This is services page")

def contact(request):
    if request.method=="POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        desc = request.POST.get("desc")
        contact=Contact(name=name, email=email, phone=phone, desc=desc,date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent.')

    
    return render(request, "contact.html")
    # return HttpResponseGone("This is contact page")