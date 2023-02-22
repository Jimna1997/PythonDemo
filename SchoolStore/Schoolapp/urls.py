
from django.contrib import admin
from . import views
from django.urls import path,include
app_name='Schoolapp'

urlpatterns = [
    path('',views.home,name='home'),
    path("register",views.register,name='register'),
    path("login",views.login,name='login'),
    path("student", views.student, name='student'),
    path("logout", views.logout, name='logout'),
    path('department/<int:deptid>/',views.department,name='department'),
]
