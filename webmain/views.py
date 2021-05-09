from django.shortcuts import render
from django.http import HttpResponse
from webmain.models import Employee,Employer
# Create your views here.

def index(request):
    return render(request,'index.html')


def employeehome(request):
    employee=Employee.objects.filter(user=request.user)
    name=employee[0].name
    return render(request,"employeehome.html",{'name':name,})

def employerhome(request):
    employer=Employer.objects.filter(user=request.user)
    name=employer[0].name
    # announced=announcement.objects.all
    return render(request,"employerhome.html",{'name':name})