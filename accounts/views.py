from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib import messages
from django.http import HttpResponse
from webmain.models import Employee,Employer,extendedUser

# Create your views here.


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            employee = Employee.objects.filter(user=request.user)
            if user.is_superuser == False:
                newuser = extendedUser.objects.filter(user=request.user)
                if newuser[0].isEmployee == True:
                    # teacher session
                    employee = Employee.objects.filter(user=user)
                    # return render(request,'index.html',{'teach':1})
                    return redirect('/employeehome')
                elif newuser[0].isEmployer == True:
                    # Student session
                    employer = Employer.objects.filter(user=user)
                    # return render(request,'index.html')
                    return redirect('/employerhome')
            else:
                return redirect("/")
            return redirect("/")
        else:
            messages.info(request, "Invalid credentials")
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

# Teacher registraion part
# Compleated

def employeereg(requests):
    if requests.method == 'POST':

        username = requests.POST['username']
        password1 = requests.POST['password1']
        password2 = requests.POST['password2']
        name = requests.POST['name']
        address = requests.POST['address']
        phnumber = requests.POST['phnumber']
        wages = requests.POST['wages']
        qualification = requests.POST['qualification']
        job = requests.POST['job']
        experience = requests.POST['experience']
        flink = requests.POST['flink']
        pin=requests.POST['pin']
        email=requests.POST['email']

        # Verification part

        if password1 != password2:
            messages.info(requests, "Password error")
            return redirect('employeereg')
        elif User.objects.filter(username=username).exists():
            messages.info(requests, "Username already exists")
            return redirect('employeereg')
        elif User.objects.filter(email=email).exists():
            messages.info(requests, "Email already exists")
            return redirect('employeereg')
        try:
            user = User.objects.create_user(
                username=username, password=password1, first_name=name,email=email)
            user.save()
            newExtendedUser = extendedUser(
                user=user, isEmployee=False, isEmployer=False, request_for='Employee')
            newEmployee = Employee(name=name, phnumber=phnumber,
                                 qualification=qualification, user=user,job=job,address=address,wages=wages,flink=flink,experience=experience,pin=pin)
            newEmployee.save()
            newExtendedUser.save()
            auth.logout(requests)
            messages.info(requests, 'User registered')
        except:
            messages.info(requests, 'Unexpected error')
    return render(requests, 'employeereg.html')


def employerreg(requests):
    if requests.method == 'POST':

        name = requests.POST['name']
        address = requests.POST['address']
        phnumber = requests.POST['phnumber']
        email=requests.POST['email']
        pin=requests.POST['pin']
        username = requests.POST['username']
        password1 = requests.POST['password1']
        password2 = requests.POST['password2']
        # Verification part

        if password1 != password2:
            messages.info(requests, "Password error")
            return redirect('employerreg')
        elif User.objects.filter(username=username).exists():
            messages.info(requests, "Username already exists")
            return redirect('employerreg')
        elif User.objects.filter(email=email).exists():
            messages.info(requests, "Email already exists")
            return redirect('employerreg')
        try:
            user = User.objects.create_user(
                username=username, password=password1, first_name=name, last_name='', email=email)
            user.save()
            newExtendedUser = extendedUser(
                user=user,isEmployee=False, isEmployer=False,request_for='Employer')
            newExtendedUser.save()
            newEmployer = Employer( user=user,name=name,address=address,
                                 phnumber=phnumber, pin=pin)
            newEmployer.save()
            auth.logout(requests)
            messages.info(requests, 'User registered')
        except:
            messages.info(requests, 'Unexpected error')
    return render(requests, 'employerreg.html')


def search(requests):
    if requests.method=='GET' :
        if requests.user.is_authenticated == True:
            return render(requests, 'empserach.html')
        else:
            return redirect("login")
    elif requests.method=='POST' :
        pin=requests.POST['pin']
        job=requests.POST['job']
        emp=Employee.objects.filter(pin=pin,job=job)
        try:
            return render(requests,'showemp.html',{'emp':emp})
            # return HttpResponse(emp)
        except:
            return HttpResponse("Error viewing Employee")
    else:
        return redirect("login")
    
    # return render(requests, 'empserach.html')
    # return redirect("login")

def showemp(request):
        if requests.user.is_authenticated == True:
            return render(request, 'showemp.html')
        else:
            return redirect("login")
        
#     return HttpResponse("Hi")