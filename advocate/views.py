from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login as auth_login,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from Admin_user.models import CaseRegister,Todo_list,Advocate,Notification
from Admin_user.form import TodolistFrom
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
        return HttpResponse("advocate home"+request.user.username+"   "+str(request.user.username[2:].isnumeric() and request.user.username[:2]=="ad"))
    

def check_user_is_advocate(request):
    return request.user.username[2:].isnumeric() and request.user.username[:2]=="ad"

def getadvocateid(request):
    return request.user.username[2:] 
def case(request):
    
    context={"username":getadvocatename(request)}
    if getnotifications(request):
        context.update(getnotifications(request))
        print(getnotifications(request)) 
    context["case"]=True
    context["data"]=CaseRegister.objects.all().filter(advocate_id=getadvocateid(request))
    return render(request,"advocate/case.html",context)

def contact(request):
    context={}
    context["contact"]=True
    contact=[]
    cases=CaseRegister.objects.all().filter(advocate_id=getadvocateid(request))
    for i in cases:
        dict={}
        dict["name"]=i.client_name
        dict["email"]=i.client_name.email
        dict["phone"]=i.client_name.phone
        dict["case"]=i.case_number
        contact.append(dict)
    context["contact"]=contact
    return render(request,"advocate/contact.html",context)

def notification(request):
    pass

def todolist(request):
    context={}
    context["todo_list"]=True
    data=Todo_list.objects.all()
    context["data"]=data
    context["form"]=TodolistFrom()
    return render(request,"advocate/todo.html",context)        

def getadvocatename(request):
    id=int(request.user.username[2:])
    return Advocate.objects.get(id=id).name;

def getnotifications(request):
    context={}
    if Notification.objects.filter(user_id=request.user.id).exists():
        context["notification"]=Notification.objects.all().filter(user_id=request.user.id)
        context["nonotification"]=Notification.objects.all().filter(user_id=request.user.id).count()
        
        return context
    else :
        return False 
