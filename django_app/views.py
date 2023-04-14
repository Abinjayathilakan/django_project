
from django.shortcuts import render,redirect,get_object_or_404
from django_app.models import Course
from django_app.models import StudentDetails,Usermember
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
import os

# Create your views here.
def form(request):
    return render(request,'form.html')

def add_admin(request):
    return render(request, 'admin.html')

def base(request):
    return render(request,'base.html')

def add_course(request):
    return render(request, 'add_course.html')


def add_coursedb(request):
    if request.method=="POST":
        course_name=request.POST.get('course')
        course_fee=request.POST.get('fee')
        course=Course(course_name=course_name,fee=course_fee)
        course.save()
        return redirect('addstudents')
    
def addstudents(request):
    courses=Course.objects.all()
    return render(request,'addstudents.html',{'course':courses})

def add_studentdb(request):
    if request.method=="POST":
        student_name=request.POST['name']
        print(student_name)
        student_address=request.POST['address']
        print(student_address)
        age=request.POST['age']
        print(age)
        jdate=request.POST['jdate']
        print(jdate)
        sel=request.POST['sel']
        print(sel)
        course1=Course.objects.get(id=sel)
        print(course1)
        student=StudentDetails(student_name=student_name,student_address=student_address,student_age=age,joining_date=jdate,course=course1)
        student.save()
        return redirect('show_student')
    
def show_student(request):
    student=StudentDetails.objects.all()
    return render(request,'show_student.html',{'students':student})


def editpage(request, pk):
    student = get_object_or_404(StudentDetails, id=pk)
    courses = Course.objects.all()

    if request.method == "POST":
        student_name = request.POST['name']
        student_address = request.POST['address']
        age = request.POST['age']
        jdate = request.POST['jdate']
        sel = request.POST['sel']
        course1 = Course.objects.get(id=sel)

        # Update student object with new data
        student.student_name = student_name
        student.student_address = student_address
        student.student_age = age
        student.joining_date = jdate
        student.course = course1
        student.save()

        return redirect('/show_student')
    else:
        return render(request, 'editpage.html', {'stud': student, 'course': courses})
    
def deletepage(request,pk):
    delete_student=StudentDetails.objects.get(id=pk)
    delete_student.delete()
    return redirect('show_student')

# def add_admins(request):
#     if request.method=="POST":
#         username=request.POST['u_name']
#         password=request.POST['password']
#         user = auth.authenticate(username=username,password=password)
        
#         if user is not None:
#             if user.is_staff:
#                 auth.login(request,user)
#                 messages.info(request,f'welcome{username}')
#                 return redirect('teacher_home')
#             else:
#                 login(request,user)
#                 auth.login(request,user)
#                 return redirect('signup')
#         else:
#             return redirect('/')
#     return redirect('home.html')

def add_admins(request):
    if request.method=="POST":
        username=request.POST['u_name']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect('add_admin')
            else:
                login(request,user)
                auth.login(request,user)
                messages.info(request,f'Welcome {username}')
                return redirect('teacher_home')
        else:
            messages.info(request,"Invalid username or password")
            return redirect('/')
    return render(request,'form.html')

      
      
def signup(request):
    courses=Course.objects.all()
    return render(request,'signup.html',{'course':courses})

def add_teacherdb(request):
    if request.method=="POST":
        firstname=request.POST.get('fname')
        lastname=request.POST.get('lname')
        username=request.POST.get('uname')
        password=request.POST.get('password')
        cpassword=request.POST.get('c_password')
        address=request.POST.get('address')
        age=request.POST.get('age')
        email=request.POST.get('mail')
        number=request.POST.get('number')
        sel=request.POST.get('sel')   
        course1=Course.objects.get(id=sel)
        image=request.FILES.get('file')
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'This username is already exists!!!!')
                return redirect('signup')
            else:
                user=User.objects.create_user(first_name=firstname,last_name=lastname,username=username,password=password,email=email)
                user.save()
                u = User.objects.get(id=user.id)
                
                member = Usermember(address=address,age=age,number=number,image=image,user=u,course=course1)
                member.save()
                return redirect('/')
        else:
            messages.info(request,'Password doesmot match...!!!')
            return redirect('signup')
    else:
        return redirect('form')
    
def teacher_home(request):
    return render(request,'teacher_home.html')

def see_profile(request):
    return render(request,'see_profile')

def teacher_profile(request):
    user_id=request.user.id
    see=Usermember.objects.get(user=user_id)
    return render(request,'see_profile_teacher.html',{'sees':see})
       


def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect('form')
    
def show_teacher(request):
    teacher=Usermember.objects.all()
    return render(request,'show_teacher.html',{'teach':teacher})
    
    
def edit_teacher(request):
    see=Usermember.objects.all()
    return render(request,'edit_teacher.html',{'show':see})

def editdb(request):
    current_user=request.user.id
    print(current_user)
    user1=Usermember.objects.get(user_id=current_user)
    user2=User.objects.get(id=current_user)
    if request.method=='POST':
        if len(request.FILES)!=0:
            if len(user1.image)>0:
                os.remove(user1.image.path)
            user1.image=request.FILES.get('file')
        user2.first_name=request.POST['fname']
        user2.last_name=request.POST['lname']
        user2.username=request.POST['uname']
        user2.email=request.POST['mail']
        user1.age=request.POST['age']
        user1.address=request.POST['address']
        user1.number=request.POST['number']
        user1.save()
        user2.save()
        return redirect('teacher_profile')
    return render(request,'edit_teacher.html',{'users':user1})
