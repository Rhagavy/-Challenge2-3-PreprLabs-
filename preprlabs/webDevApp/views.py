from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.template.defaulttags import register
from django.contrib.auth import login,authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import  User,Project

# Create your views here.
@login_required(login_url="login")
def dashPage(request):
    
    projects = Project.objects.filter(owner = request.user.id)
    context={'projects':projects}
    return render(request, "index.html",context)

def userDataPage(request):
    user = User.objects.get(id=request.user.id)
    context={'user':user}
    return render(request, "user_data.html",context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        print(request.POST)
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.get(email = email)
        except:
            print('Username does not exist')
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username = email, password = password)

        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            print('Username OR password is incorrect')
            messages.error(request,'Username OR password is incorrect' )

    return render(request, "login.html")

def logoutUser(request):
    logout(request)
    messages.success(request,'User was logged out!')
    return redirect('login')

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','user_type','language', 'password1', 'password2']    

def registerPage(request):
    form = RegisterForm()

    if request.method == 'POST':
        print(request.POST)
        form = RegisterForm(request.POST)

        #check to see if regestration info is valid
        if form.is_valid():
            print("form was valid")
            user = form.save(commit=False)
            user.username = user.email
            user.save()
            #form.save()
            messages.success(request,"Successfully created account")
            print("form saved")
            # login(request, user)

    #field Name that will passed to the form and how it will appear
    fieldNames = {'first_name':"First Name",'last_name':"Last Name",'email':"Email Address", 'password1':"Password", 'password2':"Re-type Password",'language':"language",'user_type':"User Type",}

    return render(request,"register.html", {"form":form,"fieldNames":fieldNames})

@register.filter
def get_value(dictionary, key):
    return dictionary.get(key)

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['projectName', 'projectOverview','bannerImage','startDate','recruitingStatus','slug','type','category','stage','projectStatus']


def createProjectPage(request):
    form = ProjectForm()
    #print(request.user.id)
    
    if request.method == "POST":
        #print(request.POST)
        print(request.FILES)
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            print('valid')
            project = form.save(commit=False)
            
            project.owner = User.objects.get(id=request.user.id)
            #request.user.id #logged in user
            project.save()

            return redirect('dashboard')
        else:
            print("errors:")
            print(form.errors.as_data())

    fieldNames = {'projectName':"Project Name",'projectOverview':"Project Overview",'startDate':"Project Start Date", 'recruitingStatus':"Recruiting Status", 'slug':"Project Slug",'type':"Type",'category':"Category",'stage':"Stage",'projectStatus':"Project Status"}

    context={'form':form}
    return render(request, "create_project.html",context)
    

# @login_required(login_url="login")
# def dashboardPage(request):
#     context={}
#     return render(request,"dashboard.html",context)