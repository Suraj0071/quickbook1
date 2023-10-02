from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from .forms import *

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
            
            # print(username)
            
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
        # print(user, username, password, "OOOO")
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admin_home')  # Redirect to staff-specific page
            else:
                # return redirect('doctorDashboard')  # Redirect to regular home page
                return redirect('index')  # Redirect to the 'home' URL name on successful login
        else:
            # return HttpResponse("Username or Password is incorrect!!!")
            return HttpResponse('<script>alert("Username or Password is incorrect!!!"); window.location.href=" ";</script>')

    return render(request, 'auth-login-basic.html')


def adminhome(request):
    return render(request, 'admin/admin_screen.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')


def ForgotPasswordPage(request):
    
    return render(request, 'auth-forgot-password-basic.html')
