from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from .forms import *
from. models import File
import pandas as pd
from django.contrib import messages
import os
from django.core.paginator import Paginator
# Create your views here.
@login_required(login_url='login')
def profile(request):
    return render (request,'profile.html')


@login_required(login_url='login')
def IndexPage(request):
    print(request.user, 'okoko')
    return render(request,'index.html', {'user':request.user})


def SignupPage(request):
    if request.method == 'POST':
        form = SignupUser(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("login")
        else:
            print("Form is not valid:", form.errors)
    else:
        form = SignupUser()

    return render(request, 'auth-register-basic.html', {"form": form})
def LoginPage(request):
  
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admin_home')  # Redirect to staff-specific page
            else:
                # return redirect('doctorDashboard')  # Redirect to regular home page
                return redirect('index')  
        else:
            form = UserLoginForm(request.POST)
            print("---------------",form.errors)
            return render(request, 'auth-login-basic.html' ,{"form":form})
            
            # return HttpResponse("Username or Password is incorrect!!!")
            # return HttpResponse('<script>alert("Username or Password is incorrect!!!"); window.location.href=" ";</script>')

    return render(request, 'auth-login-basic.html')
    



@login_required(login_url='login')
def uploadfile(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
    
        if not file :
            messages.error(request, "No file uploaded. Please select a file to upload.")   
            return render(request, 'uploadfile.html')     
        filename, file_extension = os.path.splitext(file.name)
        if file_extension  not in [".xlsx",".csv",]:
            messages.error(request, "Please upload in one of these vaild file formats -  xlsx or csv ")
            return render(request, 'uploadfile.html')
    
        data = pd.read_excel(file)
        # Iterate through the rows of the DataFrame
        for index, row in data.iterrows():
            # Access data from each column for the current row
            journal = row['Journal']
            date = row['Date']
            reference = row['Reference']
            description = row['Description']
            account = row['Account']
            account_name = row['Account Name']
            debit_amount = row['Debit Amount']
            credit_amount = row['Credit Amount']
            offset_account = row['Offset Account']
            memo = row['Memo']
            department = row['Department']
            File.objects.create(
               
                journal=journal,
                date=date,
                reference=reference,
                description=description,
                account=account,
                account_name=account_name,
                debit_amount=debit_amount,
                credit_amount=credit_amount,
                offset_account=offset_account,
                memo=memo,
                department=department,
                user = request.user
            )
        return redirect("showfilesdata")
    return render(request,"uploadfile.html",)


def showfilesdata(request):
    obj = File.objects.filter(user=request.user)

    paginator = Paginator(obj,12)

    pagenumber =request.GET.get('page')
    files = paginator.get_page(pagenumber)
    return render(request, "userfiledata.html",{"files":files})


def adminhome(request):
    return render(request, 'admin/admin_screen.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')

def ForgotPasswordPage(request):
    return render(request, 'auth-forgot-password-basic.html')




