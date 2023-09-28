from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages

# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')

def IndexPage(request):
    return render(request,'index.html')



# def SignupPage(request):
#     print(request.method, "CHECK")
#     print(request.POST)
#     data=request.POST
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             print('VALID')
#             form.save()
#             return render(request, 'auth-login-basic.html')
#         else:
#             # Form validation failed, show error messages
#             messages.error(request, 'Please correct the errors below.')

#     else:
#         form = UserCreationForm()

#     return render(request, 'auth-register-basic.html', {'form': form})


def SignupPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user=User.objects.create(username=username, email=email, password=password)
        # user = authenticate(request, username=username, password=password)
        print(username, password, "OOOO")
        user.set_password(password )
        user.save()
        return render(request, 'auth-login-basic.html')
    return render(request, 'auth-register-basic.html')

    
        



def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user, username, password, "OOOO")
        if user is not None:
            login(request, user)
            # print(user,'GOIT')
            return redirect('index')  # Redirect to the 'home' URL name on successful login
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'auth-login-basic.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def ForgotPasswordPage(request):
    
    return render(request, 'auth-forgot-password-basic.html')
