from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login as auth_login,authenticate,logout as auth_logut
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .form import AdvocateForm,AddAdvocateLoginTable,CaseRegisterForm,CourtCategoryForm,CourtForm,LegalScrutinyFrom,LegalScrutinyAppointmentFrom
from .models import Advocate,CourtCategory,Court,Legalscrutiny
def error_404_view(request, exception):
    return render(request,"pages-error-404.html")
# Create your views here.
def contact(request):
    return render(request,"admin/contact.html")
def test(request):
    return render(request,"admin/main.html")
def check_user_is_admin(request):
    if not (request.user.username[2:].isnumeric() and request.user.username[:2]=="ad"):
        return True
    else :
        return False

def login(request):
    context={}
    context["title"]="Login"
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        if username and password:
            user=authenticate(request,username=username,password=password)
            if user:
                auth_login(request,user)
                return redirect("/home")
            else :
                context["message"]="invalid password"
                return render(request,"admin/login.html",context=context)
        else:
            context["message"]="Enter username and password"
            return render(request,"admin/login.html",context=context)
    return render(request,"admin/login.html",context=context)
def logout(request):
    auth_logut(request)
    return redirect("/login")


    
def home(request):
    if not request.user.is_authenticated:
        return redirect("/login")

    return render(request,"home.html",{"title":"Home"})

def add_advocate(request):
    context={}
    if not request.user.is_authenticated:
        return redirect("/login")
    if request.method=="POST":
        form=AdvocateForm(request.POST)
        form1=AddAdvocateLoginTable(request.POST)
        if form.is_valid() and form1.is_valid():
            data=form.save()
            userob=form1.save(commit=False)
            userob.username="ad"+str(data.id)
            userob.save()
            context["message"]="added"
            return render(request,"form.html",context)
        else:
            context["message"]="added"
            return render(request,"form.html",context)
    context["form"]=AdvocateForm()
    context["form1"]=AddAdvocateLoginTable()
    return render(request,"form.html",context)

def remove_advocate(request,id):
    if not request.user.is_authenticated:
        return redirect("/login")
    advocate=Advocate.objects.get(id=id)
    user=User.objects.get(username="ad"+str(advocate.id))
    user.delete()
    advocate.delete()
    return redirect("/viewadvocates")
    

def view_advocate(request):
    context={}
    context["title"]="Advocates"
    if not request.user.is_authenticated:
        return redirect("/login")
    context["data"]=Advocate.objects.all()
    return render(request,"view.html",context)



def add_third_party_advocates(request):
    pass
#
def add_case(request):
    context={}
    if not request.user.is_authenticated:
        return redirect("/login")
    if request.method=="POST":
        form=CaseRegisterForm(request.POST)
        if form.is_valid() :
            form.save()
            context["message"]="added"
            return render(request,"form.html",context)
        else:
            context["message"]="added"
            return render(request,"form.html",context)
    context["form"]=CaseRegisterForm()
    return render(request,"form.html",context)
    
def assign_case_to_advocate(request):
    pass


def contacts(request):
    pass

#contact
def contact(request):
    context={}
    context["contact"]=True
    return render(request,"admin/contact.html",context)

def contact_category(requset):
    context={}
    context["contact_category"]=True
    return render(requset,"admin/contact_category.html",context)

#client

def client(request):
    context={}
    context["client"]=True
    return render(request,"admin/client.html",context)

def client_category(request):
    context={}
    context["client_category"]=True
    return render(request,"admin/client_list.html",context)

def case(request):
    context={}
    context["case"]=True
    return render(request,"admin/case.html",context)

def addcase(request):
    context={}
    context["addcase"]=True
    return render(request,"admin/addcase.html",context)

def case_category(request):
    context={}
    context["case_category"]=True
    return render(request,"admin/case_category.html",context)

def judgement_case(request):
    context={}
    context["judgement_case"]=True
    return render(request,"admin/judgement_case.html",context)

def closed_case(request):
    context={}
    context["closed_case"]=True
    return render(request,"admin/closed_case.html",context)
#notary
def notary(request):
    context={}
    context["notary"]=True
    return render(request,"admin/notary.html",context)

def open_notary(request):
    context={}
    context["open_notary"]=True
    return render(request,"admin/notary_open.html",context)

def closed_notary(request):
    context={}
    context["closed_notary"]=True
    return render(request,"admin/notary_closed.html",context)
def add_notary(request):
    context={}
    context["add_notary"]=True
    return render(request,"admin/notary_add.html",context)
#legal scrutiny

def legal_scrutiny_clients(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    context={}
    clients=Legalscrutiny.objects.all()
    context["Legal_scrutiny_list"]=clients
    context["legal_scrutiny_clients"]=True
    return render(request,"admin/legal_scrutiny_clients.html",context)

def legal_scrutiny_add_clients(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    context={}
    context["legal_scrutiny_add_clients"]=True
    if request.method=="POST":
        form=LegalScrutinyFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/notary")
        else:
            form=LegalScrutinyFrom(request.POST)
            return render(request,"form.html",context)
    else :
        context["form"]=LegalScrutinyFrom()
        return render(request,"form.html",context)

def legal_scrutiny_add_appointmends(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    context={}
    context["legal_scrutiny_add_clients"]=True
    if request.method=="POST":
        form=LegalScrutinyAppointmentFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/notary")
        else:
            form=LegalScrutinyAppointmentFrom(request.POST)
            return render(request,"form.html",context)
    else :
        context["form"]=LegalScrutinyAppointmentFrom()
        return render(request,"form.html",context)
#court
def court_list(request):
    context={}
    context["court_list"]=True
    if not request.user.is_authenticated:
        return redirect("/login")
    context["court_list"]=Court.objects.all()
    return render(request,"admin/court_list.html",context)

def add_court(request):
    context={}
    if not request.user.is_authenticated:
        return redirect("/login")
    if request.method=="POST":
        form=CourtForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/court/list")
        else:
            form=CourtForm(request.POST)
            return render(request,"form.html",context)
    else :
        context["form"]=CourtForm()
        return render(request,"form.html",context)

def court_category(request):
    context={}
    if not request.user.is_authenticated:
        return redirect("/login")
    context['court_category_list']=CourtCategory.objects.all()
    context["court_category"]=True
    return render(request,"admin/court_category.html",context)
def add_court_category(request):
    context={}
    if not request.user.is_authenticated:
        return redirect("/login")
    context['title']="Add Court Category"
    if request.method == "POST":
        form=CourtCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/court/category")
        else:
            form=CourtCategoryForm(request.POST)
            return render(request,"form.html",context)
    else :
        context["form"]=CourtCategoryForm()
        return render(request,"form.html",context)

#todo list

def todo_list(request):
    context={}
    context["todo_list"]=True
    return render(request,"admin/todo.html",context)