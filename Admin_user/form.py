from django import forms
from .models import Advocate,CaseRegister,CourtCategory,Court,Legalscrutiny,Legalscrutiny_appointment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import DateInput
class AdvocateForm(forms.ModelForm):
    class Meta:
        model = Advocate
        fields=["name","address","phone"]
    def __init__(self,*args,**kwargs):
        super(AdvocateForm,self).__init__(*args,**kwargs)
        for i in self.fields.values():
            i.widget.attrs['class']="form-control"


class AddAdvocateLoginTable(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["password1", "password2"]
    def __init__(self,*args,**kwargs):
        super(AddAdvocateLoginTable,self).__init__(*args,**kwargs)
        for i in self.fields.values():
            i.widget.attrs['class']="form-control"

class CaseRegisterForm(forms.ModelForm):
    class Meta:
        model= CaseRegister
        fields = "__all__"
    def __init__(self,*args,**kwargs):
        super(CaseRegisterForm,self).__init__(*args,**kwargs)
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
            