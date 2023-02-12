from django.db import models

# Create your models here.
class Advocate(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    phone=models.IntegerField()
    def __str__(self) :
        return self.name

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

class CaseRegister(models.Model):
    client_name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    case_number=models.CharField(max_length=50)
    year=models.IntegerField()
    advocate=models.ForeignKey(Advocate,null=True, on_delete=models.SET_NULL)
    case_category=models.ForeignKey(CaseCategory,null=True,on_delete=models.SET_NULL)
    def __str__(self) :
        return self.client_name


class Court(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    category=models.ForeignKey(CourtCategory,null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.name

class Legalscrutiny(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Legalscrutiny_appointment(models.Model):
    client=models.ForeignKey(Legalscrutiny,null=True, on_delete=models.SET_NULL)
    date=models.DateField(auto_now=False, auto_now_add=False)