from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('search',views.search,name='search'),
    path('employeereg', views.employeereg, name='employeereg'),
    path('showemp', views.showemp, name='showemp'),
    path('employerreg', views.employerreg, name='employerreg'),
]
