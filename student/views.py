from django.http import HttpResponse
from django.shortcuts import render, redirect

from student.models import Student, Course, Clas


# Create your views here.
def index(request):
    student_list= Student.objects.all()
    return render(request,'student/index.html',{'student_list':student_list})




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
    return render(request,"elective.html")