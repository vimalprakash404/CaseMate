from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login as auth_login,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
# Create your views here.

def login(request):
    context={}
    context["title"]="Login"
    if request.method=="POST":
        email=request.POST["username"]
        password=request.POST["password"]
        if User.objects.filter(email=email).exists():
            username=User.objects.get(email=email).username
        else :
            return HttpResponse("no more user in this email")
        if username and password:
            if not (username[2:].isnumeric() and username[:2]=="ad"):
                return HttpResponse("ther is no advocates in this username ")
            user=authenticate(request,username=username,password=password)
            if user:
                auth_login(request,user)
                return redirect("/advocate/home")
            else :
                
                return HttpResponse("invalid")
        else:
            return HttpResponse("login")
    form=AuthenticationForm()
    context["form"]=form
    return render(request,"form.html",context=context)

def home(request):
    if check_user_is_advocate:
        return redirect("/advocate")
    return HttpResponse("advocate home")

def check_user_is_advocate(request):
    if not (request.user.username[2:].isnumeric() and request.user.username[:2]=="ad"):
        return False
    else :
        return True
        