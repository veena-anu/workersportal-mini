from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class extendedUser(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    isEmployee=models.BooleanField(default=False)
    isEmployer=models.BooleanField(default=False)
    request_for=models.CharField(max_length=1000,blank=True)

class Employee(models.Model):
    def __str__(self): 
        return self.name
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    name=models.CharField(max_length=255,default="")
    phnumber=models.CharField(max_length=10)
    qualification=models.CharField(max_length=1000)
    job=models.CharField(max_length=2000)
    pin=models.IntegerField()
    address=models.CharField(max_length=20000)
    experience=models.CharField(max_length=2000)
    flink=models.CharField(max_length=2000)
    wages=models.IntegerField()


class Employer(models.Model):
    def __str__(self): 
        return self.name
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    name=models.CharField(max_length=255,default="")
    phnumber=models.CharField(max_length=10)
    pin=models.IntegerField()
    address=models.CharField(max_length=10000)
