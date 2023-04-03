from django import forms
from .models import caseSections,Sections,Person,State,District,NotaryCategory,Todo_list,Advocate,CaseRegister,CaseCategory,CourtCategory,Court,Legalscrutiny,Legalscrutiny_appointment,Address,client,Client_Category,Notary
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import DateInput,TimeInput,Select

class Casesectionform(forms.ModelForm):
    class Meta:
        model = caseSections
        exclude=["case"]
    def __init__(self,*args,**kwargs):
        super(Casesectionform,self).__init__(*args,**kwargs)
        for i in self.fields.values():
            i.widget.attrs['class']="form-control"

class SectionForm(forms.ModelForm):
    class Meta:
        model = Sections
        fields="__all__"
    def __init__(self,*args,**kwargs):
        super(SectionForm,self).__init__(*args,**kwargs)
        for i in self.fields.values():
            i.widget.attrs['class']="form-control"
class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        exclude=["case","Address"]
    def __init__(self,*args,**kwargs):
        super(PersonForm,self).__init__(*args,**kwargs)
        for i in self.fields.values():
            i.widget.attrs['class']="form-control"

class Addressfr(forms.ModelForm):
    class Meta:
        model = Address
        fields="__all__"
        widgets={
            'State':Select(attrs={'onchange':"changedist()"}),
        }
    def __init__(self,*args,**kwargs):
        super(Addressfr,self).__init__(*args,**kwargs)
        for i in self.fields.values():
            i.widget.attrs['class']="form-control"
            self.fields['district'].queryset = District.objects.none()

class AdvocateForm(forms.ModelForm):
    class Meta:
        model = Advocate
        fields=["name","address","phone"]
    def __init__(self,*args,**kwargs):
        super(AdvocateForm,self).__init__(*args,**kwargs)
        for i in self.fields.values():
            i.widget.attrs['class']="form-control"
class AddAdvocateLoginTable(UserCreationForm):
    

    class Meta:
        model = User
        fields = ["password1", "password2","email"]
    def __init__(self,*args,**kwargs):
        super(AddAdvocateLoginTable,self).__init__(*args,**kwargs)
        for i in self.fields.values():
            i.widget.attrs['class']="form-control"

class CaseRegisterForm(forms.ModelForm):
    class Meta:
        model= CaseRegister
        exclude=["status","client_name"]
        widgets={
            'Filling_Date':DateInput(attrs={'type':"date",'onchange':"changedate('id_Filling_Date','id_First_hearing_date');"}),
            'First_hearing_date':DateInput(attrs={'type':"date",'onchange':"changedate('id_First_hearing_date','id_Next_hearing_date')"}),
            'Next_hearing_date':DateInput(attrs={'type':"date"}),
            'Fir_date':DateInput(attrs={'type':"date"})
        }
    def __init__(self,*args,**kwargs):
        super(CaseRegisterForm,self).__init__(*args,**kwargs)
        for i in self.fields.values():
            i.widget.attrs['class']="form-control"
class CaseCategoryFrom(forms.ModelForm):
    class Meta:
        model = CaseCategory
        fields="__all__"
    def __init__(self,*args,**kwargs):
        super(CaseCategoryFrom,self).__init__(*args,**kwargs)
        for i in self.fields.values():
            i.widget.attrs['class']="form-control"
class CourtCategoryForm(forms.ModelForm):
    class Meta:
        model=CourtCategory
        fields="__all__"
    def __init__(self,*args,**kwargs):
        super(CourtCategoryForm,self).__init__(*args,**kwargs)
        for i in self.fields.values():
            i.widget.attrs['class']="form-control"

class CourtForm(forms.ModelForm):
    class Meta:
        model=Court
        fields="__all__"
    def __init__(self,*args,**kwargs):
        super(CourtForm,self).__init__(*args,**kwargs)
        for i in self.fields.values():
            i.widget.attrs['class']="form-control"
class LegalScrutinyFrom(forms.ModelForm):
    class Meta:
        model=Legalscrutiny
        fields="__all__"
    def __init__(self,*args,**kwargs):
        super(LegalScrutinyFrom,self).__init__(*args,**kwargs)
        for i in self.fields.values():
            i.widget.attrs['class']="form-control"

class LegalScrutinyAppointmentFrom(forms.ModelForm):
    class Meta:
        model=Legalscrutiny_appointment
        fields="__all__"
        widgets={
            'date':DateInput(attrs={'type':"date"})
        }
    def __init__(self,*args,**kwargs):
            super(LegalScrutinyAppointmentFrom,self).__init__(*args,**kwargs)
            for i in self.fields.values():
                i.widget.attrs['class']="form-control"

class FormClients(forms.ModelForm):
    class Meta:
        model=client
        exclude=["Address","Category","is_case"]
    def __init__(self,*args,**kwargs):
            super(FormClients,self).__init__(*args,**kwargs)
            for i in self.fields.values():
                i.widget.attrs['class']="form-control"

class ClientFullFrom(forms.ModelForm):
    class Meta:
        model=Address
        fields="__all__"
        widgets={
            'State':Select(attrs={'onchange':"changedist()"}),
        }
    def __init__(self,*args,**kwargs):
            super(ClientFullFrom,self).__init__(*args,**kwargs)
            for i in self.fields.values():
                i.widget.attrs['class']="form-control"

class Client_Category_Form(forms.ModelForm):
    class Meta:
        model=Client_Category
        fields="__all__"
        
    def __init__(self,*args,**kwargs):
            super(Client_Category_Form,self).__init__(*args,**kwargs)
            for i in self.fields.values():
                i.widget.attrs['class']="form-control"

class TodolistFrom(forms.ModelForm):
    class Meta:
        model=Todo_list
        exclude=["user","status"]
        widgets={
            'date':DateInput(attrs={'type':"date"}),
            'time':TimeInput(attrs={'type':"time"})
        }
    def __init__(self,*args,**kwargs):
            super(TodolistFrom,self).__init__(*args,**kwargs)
            for i in self.fields.values():
                i.widget.attrs['class']="form-control"

class NotaryCategoryform(forms.ModelForm):
    class Meta:
        model=NotaryCategory
        fields="__all__"
    def __init__(self,*args,**kwargs):
        super(NotaryCategoryform,self).__init__(*args,**kwargs)
        for i in self.fields.values():
            i.widget.attrs['class']="form-control"
                
class NotaryForm(forms.ModelForm):
    class Meta:
        model=Notary
        fields="__all__"
    def __init__(self,*args,**kwargs):
            super(NotaryForm,self).__init__(*args,**kwargs)
            for i in self.fields.values():
                i.widget.attrs['class']="form-control"

# class CaseActionHearingdateForm(forms.ModelForm):
#     class Meta:
#         model=CaseActionUpateHearing
#         exclude=["caseaction"]
#     def __init__(self,*args,**kwargs):
#             super(CaseActionHearingdateForm,self).__init__(*args,**kwargs)
#             for i in self.fields.values():
#                 i.widget.attrs['class']="form-control"

# class CaseActionChangeAdvocateForm(forms.ModelForm):
#     class Meta:
#         model=CaseActionChangeAdvocate
#         exclude=["caseaction"]
#     def __init__(self,*args,**kwargs):
#             super(CaseActionChangeAdvocateForm,self).__init__(*args,**kwargs)
#             for i in self.fields.values():
#                 i.widget.attrs['class']="form-control"

# class CaseActionAdvocateAprearenceForm(forms.ModelForm):
#     class Meta:
#         model=CaseActionAdvocateAprearence
#         exclude=["caseaction"]
#     def __init__(self,*args,**kwargs):
#             super(CaseActionAdvocateAprearenceForm,self).__init__(*args,**kwargs)
#             for i in self.fields.values():
#                 i.widget.attrs['class']="form-control"

# class CaseActionHearingUpadteStatusForm(forms.ModelForm):
#     class Meta:
#         model=CaseActionHearingUpadteStatus
#         exclude=["caseaction"]
#     def __init__(self,*args,**kwargs):
#             super(CaseActionHearingUpadteStatusForm,self).__init__(*args,**kwargs)
#             for i in self.fields.values():
#                 i.widget.attrs['class']="form-control"

class Upadte_advocate_form(forms.ModelForm):
    class Meta:
        model=CaseRegister
        fields=['advocate']
    def __init__(self,*args,**kwargs):
            super(Upadte_advocate_form,self).__init__(*args,**kwargs)
            for i in self.fields.values():
                i.widget.attrs['class']="form-control"

class Upadte_hearing_date_form(forms.ModelForm):
    class Meta:
        model=CaseRegister
        fields=['Next_hearing_date']
        widgets={
             'Next_hearing_date':DateInput(attrs={'type':"date"}),
        }
    def __init__(self,*args,**kwargs):
            super(Upadte_hearing_date_form,self).__init__(*args,**kwargs)
            for i in self.fields.values():
                i.widget.attrs['class']="form-control"