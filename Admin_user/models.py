from django.db import models
from django.contrib.auth.models import User
import datetime 


class State(models.Model):
    state=models.CharField(max_length=50)
    def __str__(self):
        return self.state
    
class District(models.Model):
    state=models.ForeignKey(State, on_delete=models.CASCADE)
    district=models.CharField(max_length=50)
    def __str__(self):
        return self.district

class CourtCategory(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class CaseCategory(models.Model):
    name=models.CharField(max_length=50)
    decription=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Court(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    category=models.ForeignKey(CourtCategory,null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.name
class Address(models.Model):
    House_name=models.CharField(max_length=50)
    Place=models.CharField(max_length=50)
    City=models.CharField(max_length=50)
    State=models.ForeignKey(State, on_delete=models.CASCADE)
    district=models.ForeignKey(District, on_delete=models.CASCADE)
    Country=models.CharField(max_length=50)
    Pin=models.IntegerField()
    def __str__(self):
        return self.House_name
class Advocate(models.Model):
    name=models.CharField(max_length=50)
    address=models.ForeignKey(Address,on_delete=models.DO_NOTHING)
    phone=models.IntegerField()
    court=models.ForeignKey(Court,null=True, on_delete=models.SET_NULL)
    def __str__(self) :
        return self.name
    
status_choice=(
    ("1","open"),
    ("2","judgement"),
    ("3","closed")
)

class Client_Category(models.Model):
    Name=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    def __str__(self) :
        return self.Name
class client(models.Model):
    First_name=models.CharField(max_length=50)
    Last_name=models.CharField(max_length=50)
    Address=models.ForeignKey(Address,null=True, on_delete=models.SET_NULL)
    Category=models.CharField(max_length=50,null=True)
    is_case=models.BooleanField(default=False)
    phone=models.IntegerField(null=True)
    email=models.CharField(max_length=50,null=True)
    def __str__(self) :
        return self.First_name+" "+self.Last_name
class CaseRegister(models.Model):
    client_name=models.ForeignKey(client, on_delete=models.CASCADE)
   # address=models.CharField(max_length=50)
    case_number=models.CharField(max_length=50)
    year=models.IntegerField()
    incident=models.CharField(max_length=50,null=True)
    advocate=models.ForeignKey(Advocate,null=True,on_delete=models.SET_NULL)
    Filling_Date=models.DateField(auto_now=False, auto_now_add=False,null=True)
    First_hearing_date=models.DateField(auto_now=False, auto_now_add=False,null=True)
    Next_hearing_date=models.DateField(auto_now=False, auto_now_add=False,null=True)
    Fir_date=models.DateField(auto_now=False, auto_now_add=False,null=True)
    Fir_number=models.IntegerField(null=True)
    Fir_policeStation=models.CharField(max_length=50,null=True)
    case_category=models.ForeignKey(CaseCategory,null=True,on_delete=models.SET_NULL)
    status=models.CharField(max_length=20,choices=status_choice,null=True,default=1)
    def __str__(self) :
        return self.client_name.First_name+" "+self.client_name.Last_name
class Person(models.Model):
    case=models.ForeignKey(CaseRegister, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    types=models.CharField(max_length=50)
    Address=models.ForeignKey(Address,on_delete=models.CASCADE)    
    
Action_choice=(("created","created"),("updated","updated"),("closed","closed"))
class CaseAction(models.Model):
    case=models.ForeignKey(CaseRegister, on_delete=models.DO_NOTHING)
    action=models.CharField(max_length=50,choices=Action_choice,default=1)
    date=models.DateField(auto_now=False, auto_now_add=False,null=True)

Action_upadte_type=((1,"change hearing date"),(2,"change advocate"),(3,"update status"),(4,"advocate appeared"))
# class CaseActionUpateHearing(models.Model):
#     caseaction=models.ForeignKey(CaseAction, on_delete=models.DO_NOTHING)
#     date=models.DateField(auto_now=False, auto_now_add=False,null=True)

# class CaseActionChangeAdvocate(models.Model):
#     caseaction=models.ForeignKey(CaseAction, on_delete=models.DO_NOTHING)
#     Advocate=models.ForeignKey(Advocate, on_delete=models.DO_NOTHING)

# class CaseActionHearingUpadteStatus(models.Model):
#     caseaction=models.ForeignKey(CaseAction, on_delete=models.DO_NOTHING)
#     Advocate=models.ForeignKey(Advocate, on_delete=models.DO_NOTHING)
#     description=models.CharField(max_length=50)

# class CaseActionAdvocateAprearence(models.Model):
#     caseaction=models.ForeignKey(CaseAction, on_delete=models.DO_NOTHING)
#     advocate=models.ForeignKey(Advocate, on_delete=models.CASCADE)
#     date=models.DateField(auto_now=False, auto_now_add=False,null=True)

class Sections(models.Model):
    sections=models.CharField(max_length=50)
    def __str__(self):
        return self.sections
    

class caseSections(models.Model):
    case=models.ForeignKey(CaseRegister, on_delete=models.CASCADE)
    Sections=models.ForeignKey(Sections, on_delete=models.CASCADE)
    def __str__(self):
        return self.Sections.sections

class Legalscrutiny(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Legalscrutiny_appointment(models.Model):
    client=models.ForeignKey(Legalscrutiny,null=True, on_delete=models.SET_NULL)
    date=models.DateField(auto_now=False, auto_now_add=False)




        

    

class Todo_list(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    status=models.BooleanField(default=False)
    date=models.DateField(auto_now=False, auto_now_add=False,null=True)
    time=models.TimeField(auto_now=False, auto_now_add=False,null=True)

class NotaryCategory(models.Model):
    Name=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    def __str__(self):
        return self.Name    
STATUS_CHOICE=(("Open","Open"),("Progress","Progress"),("Close","Close"))

class Notary(models.Model):
    client_name=models.ForeignKey(client, on_delete=models.CASCADE)
    #Address=models.ForeignKey(Address,null=True, on_delete=models.SET_NULL)
    category=models.ForeignKey(NotaryCategory,null=True, on_delete=models.SET_NULL)
    file=models.FileField(upload_to="notary", max_length=1000)
    def __str__(self):
        return self.client_name
    
class Notification(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    path=models.CharField(max_length=50)
    date=models.DateField(auto_now=False, auto_now_add=False)
    time=models.TimeField(auto_now=False, auto_now_add=False)

class Judgement(models.Model):
    case=models.ForeignKey(CaseRegister, on_delete=models.CASCADE)
    date=models.DateField( auto_now=False, auto_now_add=False)
    details=models.CharField(max_length=50)

class Judgement_files(models.Model):
    judgement=models.ForeignKey(Judgement, on_delete=models.CASCADE)
    type=models.CharField(max_length=50)
    file=models.FileField(upload_to="judgement", max_length=100)