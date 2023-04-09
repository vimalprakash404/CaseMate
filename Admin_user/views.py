from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login as auth_login,authenticate,logout as auth_logut
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .form import  Casesectionform,SectionForm,PersonForm,Addressfr,Upadte_hearing_date_form,Upadte_advocate_form,NotaryCategoryform,NotaryForm ,TodolistFrom,AdvocateForm,AddAdvocateLoginTable,CaseRegisterForm,CaseCategoryFrom,CourtCategoryForm,CourtForm,LegalScrutinyFrom,LegalScrutinyAppointmentFrom,ClientFullFrom,FormClients,Client_Category_Form
from .models import caseSections,Sections,District,State,Notification, CaseAction,NotaryCategory,Todo_list,CaseCategory,CaseRegister,Advocate,CourtCategory,Court,Legalscrutiny,client as client_model ,Client_Category,Notary as NotaryModel
import json

def insertstate():
    f = open('data.json')
    data = json.load(f)
    for i in data['states']:
        print(i["state"])
        state=State.objects.create(state=i["state"])
        print("_________")
        for j in i["districts"]:
            print(j)
            District.objects.create(state=state,district=j)
    f.close()


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

def rend(request):
    context={}
    context["form"]=Addressfr()
    
    return render(request,"form.html",context)
def clienttocase(request,id):
    cli=client_model.objects.get(id=id)
    caseid=CaseRegister.objects.get(client_name=cli)
    return redirect("/case/details/"+str(caseid.id))
    

def clienttonotary(request):
    pass
def is_admin(request):
    return not request.user.username[2:].isnumeric() and request.user.username[:2]=="ad"
def home(request):
    context={"title":"Dashboard"}
    #insertstate()
    if not request.user.is_authenticated and is_admin:
        return redirect("/login")
    print("_____________________________________\n")
    print(str(CaseRegister.objects.all().count()))
    crime_type_number=[]
    crime_label=[]
    for i in CaseCategory.objects.all():
        crime_type_number.append(CaseRegister.objects.all().filter(case_category=i).count())
        crime_label.append(str(i.name))
    context["casedata"]=CaseRegister.objects.all().count()
    context["notarydata"]=NotaryModel.objects.all().count()
    context["legal_su"]=Legalscrutiny.objects.all().count()
    context["crime_type_number"]=crime_type_number
    print(crime_label)
    context["crime_label"]=crime_label
    return render(request,"admin/home.html",context)

def add_advocate(request):
    if not request.user.is_authenticated and is_admin:
        return redirect("/login")
    context={}
    if not request.user.is_authenticated:
        return redirect("/login")
    if request.method=="POST":
        form=AdvocateForm(request.POST)
        form1=AddAdvocateLoginTable(request.POST)
        form2=ClientFullFrom(request.POST)
        if form.is_valid() and form1.is_valid() and form2.is_valid():
            data=form.save(commit=False)
            data.address=form2.save()
            data.save()
            userob=form1.save(commit=False)
            userob.username="ad"+str(data.id)
            userob.save()
            context["message"]="added"
            return render(request,"form.html",context)
        else:
            context["form"]=AdvocateForm(request.POST)
            context["form1"]=AddAdvocateLoginTable(request.POST)
            context["form2"]=ClientFullFrom(request.POST)
            context["message"]="invalid data please enter details"
            return render(request,"form.html",context)
    context["form"]=AdvocateForm()
    context["form1"]=AddAdvocateLoginTable()
    context["form2"]=ClientFullFrom()
    return render(request,"form.html",context)

def remove_advocate(request,id):
    if not request.user.is_authenticated and is_admin:
        return redirect("/login")
    if not request.user.is_authenticated:
        return redirect("/login")
    advocate=Advocate.objects.get(id=id)
    user=User.objects.get(username="ad"+str(advocate.id))
    user.delete()
    advocate.delete()
    return redirect("/viewadvocates")
    

def view_advocate(request):
    if not request.user.is_authenticated and is_admin:
        return redirect("/login")
    context={}
    context["advocate"]=True
    context["title"]="Advocates"
    if not request.user.is_authenticated:
        return redirect("/login")
    context["data"]=Advocate.objects.all()
    return render(request,"admin/advocate_view.html",context)



def add_third_party_advocates(request):
    pass
#
def add_case(request):
    if not request.user.is_authenticated and is_admin:
        return redirect("/login")
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
    context["form"]=FormClients()
    context["form1"]=CaseRegisterForm()
    return render(request,"form.html",context)
    
def assign_case_to_advocate(request):
    pass


def contacts(request):
    pass

#contact
def contact(request):
    if not request.user.is_authenticated and is_admin:
        return redirect("/login")
    context={"title":"Contact"}
    context["contact"]=True
    contact=[]
    cases=CaseRegister.objects.all()
    notarys=NotaryModel.objects.all()
    for i in cases:
        dict={}
        dict["name"]=i.client_name
        dict["email"]=i.client_name.email
        dict["phone"]=i.client_name.phone
        dict["case"]=i.case_number
        contact.append(dict)
    for i in notarys:
        dict={}
        dict["name"]=i.client_name
        dict["email"]=i.client_name.email
        dict["phone"]=i.client_name.phone
        dict["notary"]=True
        contact.append(dict)
    context["contact"]=contact
    return render(request,"admin/contact.html",context)

def contact_category(request):
    if not request.user.is_authenticated and is_admin:
        return redirect("/login")
    context={}
    context["contact_category"]=True
    return render(request,"admin/contact_category.html",context)

#client

def client(request):

    if not request.user.is_authenticated and is_admin:
        return redirect("/login")
    context={"title":"Client"}
    context["client"]=True
    context["clients"]=client_model.objects.all()
    return render(request,"admin/client_list.html",context)



def add_clients(request):
    if not request.user.is_authenticated and is_admin:
        return redirect("/login")
    context={}
    context["client"]=True
    if request.method=="POST":
        form=FormClients(request.POST)
        form1=ClientFullFrom(request.POST)
        if form.is_valid() and form1.is_valid():
            address=form1.save()
            client_category_ob=form.save(commit=False)
            client_category_ob.Address=address
            client_category_ob.save()
            return redirect("/client")
        else:
            context["form"]=FormClients(request.POST)
            context["form1"]=ClientFullFrom(request.POST)
            return render(request,"form.html",context)
    else :
        context["form"]=FormClients()
        context["form1"]=ClientFullFrom()
        return render(request,"form.html",context)

def client_category(request):
    if not request.user.is_authenticated and is_admin:
        return redirect("/login")
    context={"title":"Client Category"}
    context["client_category"]=True
    context["client_category_model"]=Client_Category.objects.all()
    return render(request,"admin/client.html",context)

def add_client_category(request):
    if not request.user.is_authenticated and is_admin:
        return redirect("/login")
    context={}
    context["client_category"]=True
    if request.method=="POST":
        form=Client_Category_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/client/category")
        else:
            context["form"]=Client_Category_Form(request.POST)
            return render(request,"form.html",context)
    else :
        context["form"]=Client_Category_Form()
        return render(request,"form.html",context)

def case(request):
    if not request.user.is_authenticated and is_admin:
        return redirect("/login")
    context={"title":"Case"}
    context["case"]=True
    context["data"]=CaseRegister.objects.all()
    context["advocate_update_form"]=Upadte_advocate_form()
    context["Upadte_hearing_date_form"]=Upadte_hearing_date_form()
    return render(request,"admin/case.html",context)

def addcase(request,id):
    if not request.user.is_authenticated and is_admin:
        return redirect("/login")
    context={}
    context["addcase"]=True
    if request.method=="POST":
        form=CaseRegisterForm(request.POST)
        if form.is_valid():
            case=form.save(commit=False)
            case.client_name=client_model.objects.get(id=id)
            data=client_model.objects.get(id=id)
            data.Category="case"
            data.is_case=True
            data.save()
            case.save()
            action_case_create(str(case.id))
            return redirect("/case")
        else:
            form=CaseRegisterForm(request.POST)
            return render(request,"form.html",context)
    else :
        context["form"]=CaseRegisterForm()
        return render(request,"form.html",context)
def add_person(request,id):
    if not request.user.is_authenticated and is_admin:
        return redirect("/login")
    context={}
    context["add_person"]=True
    if request.method=="POST":
        form=PersonForm(request.POST)
        form2=Addressfr(request.POST)
        if form.is_valid()and form2.is_valid():
            data=form.save(commit=False)
            data2=form2.save()
            data.Address=data2
            data.case=CaseRegister.objects.get(id=id)
            data.save()
            return redirect("/case/category")
        else:
            form=PersonForm(request.POST)
            form2=Addressfr(request.POST)
            context["form"]=PersonForm(request.POST)
            context["form1"]=Addressfr(request.POST)
            return render(request,"form.html",context)
    else :
        context["form"]=PersonForm()
        context["form1"]=Addressfr()
        return render(request,"form.html",context)
    
def case_category(request):
    if not request.user.is_authenticated and is_admin:
        return redirect("/login")
    context={"title":"Case Category"}
    context["case_category"]=True
    context["data"]=CaseCategory.objects.all()
    return render(request,"admin/case_category.html",context)

def case_category_add(request):
    if not request.user.is_authenticated and is_admin:
        return redirect("/login")
    context={}
    context["case_category"]=True
    if request.method=="POST":
        form=CaseCategoryFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/case/category")
        else:
            form=CaseCategoryFrom(request.POST)
            return render(request,"form.html",context)
    else :
        context["form"]=CaseCategoryFrom()
        return render(request,"form.html",context)
def case_edit_edit(request,id):
    context={}
    context["addcase"]=True
    if request.method=="POST":
        form=CaseRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/case")
        else:
            form=CaseRegisterForm(request.POST)
            return render(request,"form.html",context)
    else :
        ob=CaseRegister.objects.get(id=id)
        context["form"]=CaseRegisterForm(instance=ob)
        return render(request,"form.html",context)
    
def case_details(request,id):
    ob=CaseRegister.objects.get(id=id)
    context={}
    context["data"]=ob
    context["form"]=Casesectionform()
    context["actions"]=CaseAction.objects.filter(case=ob)
    context["sections"]=caseSections.objects.all().filter(case=ob)
    return render(request,"admin/case_details.html",context)

def upadte_hearing_details(request,id):
    if request.method=="POST":
        form=Upadte_hearing_date_form(request.POST)
        if form.is_valid():
            data=form.save(commit=False)
            data1=CaseRegister.objects.get(id=id)
            data1.Next_hearing_date=data.Next_hearing_date
            data1.save()
            action_case_hearing_update(id,data.Next_hearing_date)
            return redirect("/case")
        else:
            return redirect("/case")
    else:
        return redirect("/case")
def update_advocate(request,id):
    if request.method=="POST":
        form=Upadte_advocate_form(request.POST)
        if form.is_valid():
            data=form.save(commit=False)
            data1=CaseRegister.objects.get(id=id)
            oldadvocate=Advocate.objects.get(id=data1.advocate.id)
            data1.advocate=data.advocate
            data1.save()
            action_change_advocate(id,data.advocate,oldadvocate)
            return redirect("/case")
        else:
            return redirect("/case")
    else:
        return redirect("/case")
    
    
def close_case(request,id):
    data=CaseRegister.objects.get(id=id)
    action_case_close(id)
    return redirect("/case")
from .models import CaseAction
from datetime import date
import time

t = time.localtime()
time.strftime("%H:%M:%S", t)
def addcaseaction(case_id,action,date):
    CaseAction.objects.create(case_id=case_id,action=action,date=date)
from advocate.views import getadvocateid
def  action_change_advocate(case_id,advocate,oldadvocate_id):
    oldadvocate=oldadvocate_id
    newadvocate=advocate
    addcaseaction(case_id=case_id,action="advocate changed"+oldadvocate.name + "to "+newadvocate.name +"",date=date.today())
    addnotification(user_id="ad"+str(oldadvocate.id),title="advocate changed",descrption="advocate changed"+oldadvocate.name + "to "+newadvocate.name +"",date=date.today(),time=time.strftime("%H:%M:%S", t),path="/case/details/"+str(case_id))

def action_advocate_appreance(case_id,advocate_id):
    advocate=Advocate.object.get(id=advocate_id)
    addcaseaction(case_id=case_id,action="case was appeared by"+advocate.name,date=date.today())

def action_case_create(id):
    addcaseaction(case_id=id,action="case created",date=date.today())

def action_case_hearing_update(case_id,date_para):
    addcaseaction(case_id=case_id,action="hearing date updated to"+str(date_para),date=date.today())

def action_case_close(case_id):
    addcaseaction(case_id=case_id,action="case closed",date=date.today())

    
#each action feature
# from datetime import date
# def case_action_create(caseid):
#     print(str(date.today()))
#     caseaction=CaseAction.objects.create(case_id=caseid,action="created",date=str(date.today()))

# def case_action_close(caseid):
#     caseaction=CaseAction.objects.create(case_id=caseid,action="closed")


# def case_action_update():
#     pass
# from .form import CaseActionHearingUpadteStatusForm,CaseActionAdvocateAprearenceForm,CaseActionChangeAdvocateForm,CaseActionHearingdateForm


# def action_change_next_hearing_date(request,caseid,date_arg):
#     # case=CaseRegister.objects.get(id=caseid)
#     # case.Next_hearing_date=date_arg
#     # case.save()
#     # caseaction=CaseAction.objects.create(case=case,action="updated",date=date.today())
#     # case_hearing_update=CaseActionUpateHearing.objects.create(caseaction=caseaction,date=date_arg)
#     # case_hearing_update.save()
#     context={}
#     context["a"]=True
#     if request.method=="POST":
#         form=CaseActionHearingdateForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("/case/category")
#         else:
#             form=CaseActionHearingdateForm(request.POST)
#             return render(request,"form.html",context)
#     else :
#         context["form"]=CaseActionHearingdateForm()
#         return render(request,"form.html",context)
#     pass

# from .models import CaseActionChangeAdvocate
# def action_change_advocate(request,caseid,advocateid):
#     case=CaseRegister.objects.get(id=caseid)
#     ad=Advocate.object.get(id=advocateid)
#     case.advocate=ad
#     case.save()
#     caseaction=CaseAction.objects.create(case=case,action="updated",date=date.today())
#     case_hearing_update=CaseActionChangeAdvocate.objects.create(caseaction=caseaction,Advocate=ad)
#     case_hearing_update.save()

# def action_apprearence_advocate(request,caseid,date_arg):
#     case=CaseRegister.objects.get(id=caseid)
#     caseaction=CaseAction.objects.create(case=case,action="updated",date=date.today())
#     case_hearing_update=CaseActionChangeAdvocate.objects.create(caseaction=caseaction,Advocate=case.advocate,date=date_arg)
#     case_hearing_update.save()

def action_update_progress(request):
    pass


def case_action_close(caseid):
    caseaction=CaseAction.objects.create(case_id=caseid,action="closed",date=str(date.today()))


def judgement_case(request):
    if not request.user.is_authenticated and is_admin:
        return redirect("/login")
    context={"title":"Judgement Case"}
    
    context["case"]=True
    context["data"]=CaseRegister.objects.all().filter(status="1")
    context["advocate_update_form"]=Upadte_advocate_form()
    context["Upadte_hearing_date_form"]=Upadte_hearing_date_form()
    return render(request,"admin/case.html",context)

def closed_case(request):
    if not request.user.is_authenticated and is_admin:
        return redirect("/login")
    context={"title":"Closed Case"}
    context["case"]=True
    context["data"]=CaseRegister.objects.all().filter(status="2")
    context["advocate_update_form"]=Upadte_advocate_form()
    context["Upadte_hearing_date_form"]=Upadte_hearing_date_form()
    return render(request,"admin/case.html",context)

def notary(request):
    if not request.user.is_authenticated and is_admin:
        return redirect("/login")
    context={"title":"Notary"}
    context["notary"]=True
    context["data"]=NotaryModel.objects.all()
    return render(request,"admin/notary.html",context)
def notary_category(request):
    if not request.user.is_authenticated and is_admin:
        return redirect("/login")
    context={"title":"Notary Category"}
    context["notary_category"]=True
    context["data"]=NotaryCategory.objects.all()
    if request.method=="POST":
        form=NotaryCategoryform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("notary_category")
        else:
            form=NotaryCategoryform(request.POST)
            return render(request,"admin/notarycategory.html",context)
    else :
        context["form"]=NotaryCategoryform()
        return render(request,"admin/notarycategory.html",context)

def notary_add_category(request):
    if not request.user.is_authenticated and is_admin:
        return redirect("/login")
    context={}
    context["notary"]=True
    if request.method=="POST":
        form=NotaryCategoryform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/notary")
        else:
            form=NotaryCategoryform(request.POST)
            return render(request,"admin/notarycategory.html",context)
    else :
        context["form1"]=NotaryCategoryform()
        return render(request,"admin/notarycategory.html",context)
def open_notary(request):
    if not request.user.is_authenticated and is_admin:
        return redirect("/login")
    context={"title":"Notary"}
    context["open_notary"]=True
    context["data"]=NotaryModel.objects.all()
    if request.method=="POST":
        form=NotaryForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/notary/open")
        else:
            form=NotaryForm(request.POST,request.FILES)
            return render(request,"admin/notarycategory.html",context)
    else :
        context["form1"]=NotaryForm(request.POST,request.FILES)
    return render(request,"admin/notary_open.html",context)
def notary_change_status(requset,id,status):
    ob=NotaryModel.objects.get(id=id)
    
    return  redirect("notary")
def progress_notary(request):
    context={}
    return render(request,"admin/notary_prgoress.html",context)
def closed_notary(request):
    context={}
    context["closed_notary"]=True
    if NotaryModel.objects.filter(status="Close").exists():
        context["data"]=NotaryModel.objects.all().filter(status="Close")
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
        return redirect("/loDateInputgin")
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
    context={"title":"Court"}
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
    context={"title":"Court Category"}
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
    if not request.user.is_authenticated and is_admin:
        return redirect("/login")
    context={"title":"Todo"}
    context["todo_list"]=True
    data=Todo_list.objects.all()
    context["data"]=data
    context["form"]=TodolistFrom()
    return render(request,"admin/todo.html",context)

def addtodolist(request):
    if not request.user.is_authenticated and is_admin:
        return redirect("/login")
    context={}
    context["todo_list"]=True
    if request.method == "POST":
        form=TodolistFrom(request.POST)
        if form.is_valid():
            data=form.save(commit=False)
            data.user=request.user
            data.status=False
            data.save()
            return todo_list(request)
        else:
            form=TodolistFrom(request.POST)
            return todo_list(request)
    else :
        context["form"]=TodolistFrom()
        return todo_list(request)

def done_status_todolist(request,id):
    context={}
    context["todo_list"]=True
    ob=Todo_list.objects.get(id=id)
    ob.status=True
    ob.save()
    return redirect("todo_list")


def addnotification(user_id,title,descrption,date,path,time):
    user=User.objects.get(username=user_id)
    Notification.objects.create(user=user,title=title,description=descrption,date=date,time=time,path=path)
from django.http import JsonResponse

def get_district(request,id):
    ss=District.objects.filter(state_id=id)
    data={}
    for i in ss:
        data.update({str(i.id):str(i.district)})
    return JsonResponse(data)

def sections(request):
    ob=Sections.objects.all()
    context={"sections":ob}
    if request.method=="POST":
        form= SectionForm(request.POST)
        if form.is_valid():
            form.save()
            context={"sections":ob}
            return render(request,"admin/sections.html",context)
        else:
            context["form"]=SectionForm(request.POST)
            return render(request,"admin/sections.html",context)
    else:
        context["form"]=SectionForm(request.POST)
        return render(request,"admin/sections.html",context)

def addcasesections(request,id):
    if request.method=="POST":
        form=Casesectionform(request.POST)
        if form.is_valid():
            data=form.save(commit=False)
            data.case=CaseRegister.objects.get(id=id)
            if caseSections.objects.filter(Sections=data.Sections).exists():
                return redirect("/case/details/"+str(id))
            data.save()
            return redirect("/case/details/"+str(id))
        else:
            return redirect("/case/details/"+str(id))
            
    else:
        return redirect("/case/details/"+str(id))

def removecasesections(request,id):
    case_id=caseSections.objects.get(id=id).case.id
    caseSections.objects.get(id=id).delete()
    return redirect("/case/details/"+str(case_id))
