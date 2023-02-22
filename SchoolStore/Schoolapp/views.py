from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.views.decorators.csrf import csrf_protect
from Schoolapp.models import Department, Student


# Create your views here.
def home(request):
    dept_list = Department.objects.all()
    return render(request,'home.html',{'dept_list':dept_list})

def department(request,deptid):
    depart = Department.objects.get(id=deptid)
    return render(request,'department.html',{'depart':depart})

def login(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/student')
            else:
                messages.info(request, 'Invalid credentials')
                return redirect('login')
        else:
            return render(request, 'login.html')

def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password']
        password1=request.POST['password1']
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username taken")
                return redirect('/register')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,password=password)
                user.save();
                print('User created')
                return redirect('/login')
        else:
            messages.info(request,"Password doesn't match")
            return redirect('/register')
    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

@csrf_protect
def student(request):
    student1=Student.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        # dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phn_no = request.POST.get('phn_no')
        dept = request.POST.get('dept')
        course = request.POST.get('course')
        purpose = request.POST.get('purpose')
        materials = request.POST.getlist('materials')
        student = Student(name=name,course=course,age=age,gender=gender,email=email,address=address,phn_no=phn_no,dept=dept,purpose=purpose,materials=materials)
        student.save()
    return render(request,'student.html',{'student1':student1})

# def student(request):
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = Student(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             if User.objects.filter(name=form.cleaned_data['name']).exists():
#                 return render(request, '/student', {'form': form,'error_message': 'Username already exists.'})
#             elif User.objects.filter(email=form.cleaned_data['email']).exists():
#                 return render(request, '/student', {'form': form,'error_message': 'Email already exists.'})
#             else:
#                 # Create the user:
#                 user = User.objects.create_user(
#                     form.cleaned_data['username'],
#                     form.cleaned_data['email'],
#                     form.cleaned_data['password']
#                 )
#                 user.first_name = form.cleaned_data['first_name']
#                 user.last_name = form.cleaned_data['last_name']
#                 user.phone_number = form.cleaned_data['phone_number']
#                 user.save()
#
#                 # Login the user
#                 login(request, user)
#
#                 # redirect to accounts page:
#                 return HttpResponseRedirect('/mymodule/account')
#
#     # No post data availabe, let's just show the page.
#     else:
#         form = RegisterForm()
#
#     return render(request, 'student.html', {'form': form})