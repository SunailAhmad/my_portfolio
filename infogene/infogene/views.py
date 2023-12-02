from operator import index
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    
    return render(request, "index.html")

def about_me(request):
    return render(request,"about-me.html")

def contact(request):
    try:
        data={}
        fname=request.GET.get('firstname')
        lname=request.GET.get('lastname')
        email=request.GET.get('email')
        phone=request.GET.get('phonenumber')
        message=request.GET.get('message')
        data={
            'fname':firstname,
            'lname':lastname,
            'email':email,
            'phone':phonenumber,
            'message':message

        }
        return render(request,"contact.html",data)
    except:
        return render(request,"contact.html")
    

    return render(request,"contact.html")

def projects(request):
    return render(request,"projects.html")
    
