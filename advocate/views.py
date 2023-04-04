from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login as auth_login,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from Admin_user.models import CaseRegister,Todo_list,Advocate,Notification
from Admin_user.form import TodolistFrom
# Create your views here.
def dashbord(request):
    return render(request,"advocate/home.html")
def adv_login(request):
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
    return render(request,"advocate/login.html",context=context)

def adv_home(request):
        return HttpResponse("advocate home"+request.user.username+"   "+str(request.user.username[2:].isnumeric() and request.user.username[:2]=="ad"))
    

def check_user_is_advocate(request):
    return request.user.username[2:].isnumeric() and request.user.username[:2]=="ad"

def getadvocateid(request):
    return request.user.username[2:] 


from Admin_user.form import Upadte_advocate_form,Upadte_hearing_date_form

def adv_case(request):
    
    context={"username":getadvocatename(request)}
    if getnotifications(request):
        context.update(getnotifications(request))
        print(getnotifications(request)) 
    context["case"]=True
    context["data"]=CaseRegister.objects.all().filter(advocate_id=getadvocateid(request))
    context["advocate_update_form"]=Upadte_advocate_form()
    context["Upadte_hearing_date_form"]=Upadte_hearing_date_form()
    return render(request,"advocate/case.html",context)
from datetime import date
def action_case_hearing_update(case_id,date_para):
    addcaseaction(case_id=case_id,action="hearing date updated to"+str(date_para),date=date.today())
from Admin_user.models import *
def addcaseaction(case_id,action,date):
    CaseAction.objects.create(case_id=case_id,action=action,date=date)
def  action_change_advocate(case_id,advocate,oldadvocate_id):
    oldadvocate=oldadvocate_id
    newadvocate=advocate
    addcaseaction(case_id=case_id,action="advocate changed"+oldadvocate.name + "to "+newadvocate.name +"",date=date.today())
    #addnotification(user_id="ad"+str(oldadvocate.id),title="advocate changed",descrption="advocate changed"+oldadvocate.name + "to "+newadvocate.name +"",date=date.today(),time=time.strftime("%H:%M:%S", t),path="/case/details/"+str(case_id))

def action_case_close(case_id):
    addcaseaction(case_id=case_id,action="case closed",date=date.today())
def ad_upadte_hearing_details(request,id):
    if request.method=="POST":
        form=Upadte_hearing_date_form(request.POST)
        if form.is_valid():
            data=form.save(commit=False)
            data1=CaseRegister.objects.get(id=id)
            data1.Next_hearing_date=data.Next_hearing_date
            data1.save()
            action_case_hearing_update(id,data.Next_hearing_date)
            return redirect("adv_case")
        else:
            return redirect("adv_case")
    else:
        return redirect("adv_case")

def ad_close_case(request,id):
    data=CaseRegister.objects.get(id=id)
    action_case_close(id)
    return redirect("adv_case")

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
