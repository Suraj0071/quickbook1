from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from .forms import *
from. models import File
import pandas as pd

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
        UserRegister = SignupUser(request.POST)
        print("user is validating")
        if UserRegister.is_valid():
            user = UserRegister.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("login")
        
        messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        UserRegister = SignupUser()
        
    return render(request, 'auth-register-basic.html',{'UserRegister':UserRegister})


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
            # return HttpResponse("Username or Password is incorrect!!!")
            return HttpResponse('<script>alert("Username or Password is incorrect!!!"); window.location.href=" ";</script>')

    return render(request, 'auth-login-basic.html')
    



@login_required(login_url='login')
def uploadfile(request):
   
    if request.method == 'POST':
        file = request.FILES.get('file')
        data = pd.read_excel(file)
        column_names = data.columns.tolist()
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
            
            # Now you can print or use the data as needed
       
            # ... Print other values similarly ...
            
            # Create a File object with the extracted data
            File.objects.create(
                user=request.user,
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
                department=department
            )
        return redirect("showfilesdate")
    return render(request,"uploadfile.html",)


def showfilesdata(request):
    files = File.objects.all()
    return render(request, "tables-basic.html",{"files":files})


def adminhome(request):
    return render(request, 'admin/admin_screen.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')


def ForgotPasswordPage(request):
    return render(request, 'auth-forgot-password-basic.html')
