from django.http import HttpResponse
from django.shortcuts import render, redirect

from student.models import Student, Course, Clas
from django.contrib import auth

# Create your views here.
def index(request):
    # if request.user.username:
    #     student_list= Student.objects.all()
    #     return render(request,'student/index.html',{'student_list':student_list})
    # else:
    #     redirect("/student/login/")
    student_list = Student.objects.all()
    return render(request, 'student/index.html', {'student_list': student_list})

def add_student(request):
    if request.method =="GET":
        class_list = Clas.objects.all()
        course_list = Course.objects.all()
        return render(request,'student/add.html',{"class_list":class_list,"course_list":course_list})
    else:
        stu = Student.objects.create(**request.POST.dict())
        return redirect('/student/index/')


def delete_student(request,del_id):
    student = Student.objects.get(pk=del_id)
    if request.method == "GET":
        return render(request,'student/delete.html',{"student":student})
    else:
        student.delete()
        return redirect("/student/index/")
def edit_student(request,edit_id):
    edit_stu = Student.objects.get(pk=edit_id)
    if request.method == "GET":
        class_list = Clas.objects.all()
        course_list = Course.objects.all()
        return render(request,"student/edit_stu.html",{"edit_stu":edit_stu,"class_list":class_list,"course_list":course_list})
    else:
        course_id_list = request.POST.getlist("course_id_list")
        #获取客户端数据
        data = request.POST.dict()
        #删除course_id_list
        data.pop("course_id_list")
        #更新一对多数据
        Student.objects.filter(pk=edit_id).update(**data)
        edit_stu.courses.set(course_id_list)
        return redirect("/student/index/")


def elective(request):
    if request.method == "GET":
        course_list = Course.objects.all()
        return render(request, "student/elective.html", {"course_list": course_list})

    else:
        print(request.POST)
        course_id_list = request.POST.getlist("course_id_list")
        stu_id = request.user.stu_id
        stu = Student.objects.get(pk=stu_id)
        stu.courses.set(course_id_list)

        return redirect("/student/index")


def search(request):
    cate = request.GET.get("cate")
    key_word = request.GET.get("key_word")
    if cate == "name":
        student_list = Student.objects.filter(name__contains=key_word)

    elif cate == "class":
        student_list = Student.objects.filter(clas__name=key_word)
    else:
        student_list=[]

    return render(request,"student/index.html",{"student_list": student_list, "key_word": key_word})
def login(request):
    if request.method == "GET":
        return render(request,"student/login.html")
    else:
        user = request.POST.get("loginUsername")
        pwd = request.POST.get("loginPassword")


        user =auth.authenticate(username=user,password=pwd)
        if user:
            auth.login(request,user)
            return redirect("/student/index/")
        else:
            return HttpResponse("/student/login/")
def logout(request):
    auth.logout(request)
    return redirect("/student/login/")