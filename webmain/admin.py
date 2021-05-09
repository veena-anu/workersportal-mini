from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Employee,Employer,extendedUser
# Register your models here.


class extendedUserAdmin(admin.ModelAdmin):
    list_display=('user','isEmployee','isEmployer','request_for')

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('user','name','phnumber','qualification','job','pin','experience','flink','wages','address')

class EmployerAdmin(admin.ModelAdmin):
    list_display=('user','name','phnumber','pin','address')



admin.site.register(extendedUser,extendedUserAdmin)
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Employer,EmployerAdmin)