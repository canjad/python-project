from django.contrib import admin

from django.urls import path,re_path
from student.views import index,add_student,delete_student,edit_student,elective,search,login,logout
urlpatterns = [
    path('index/', index),
    path('add/', add_student),
    re_path('delete/(\d+)', delete_student),
    re_path('edit/(\d+)', edit_student),

    path('elective/', elective),
    path('search/', search),
    path('login/', login),
    path('logout/',logout)
]