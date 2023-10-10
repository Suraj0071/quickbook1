from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from .forms import *
from. models import File,EmailToken
import pandas as pd
from django.contrib import messages
import os
from django.core.paginator import Paginator
from django.views import View
import uuid

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





class InvoicesView(View):
    def get(self, request):
        return render(request, "Invoices.html")
    



class Customer_statementsView(View):
    def get(self, request):
        return render(request, "customer_statements.html")
    

class CustomersView(View):
    def get(self, request):
        return render(request, "customers.html")
    


class Products_servicesView(View):
    def get(self, request):
        return render(request, "products_services.html")
    


class BillsView(View):
    def get(self, request):
        return render(request, "bills.html")
    


class VendorsView(View):
    def get(self, request):
        return render(request, "vendors.html")



class TransactionsView(View):
    def get(self, request):
        return render(request, "transactions.html")
    

class ReconciliationView(View):
    def get(self, request):
        return render(request, "reconciliation.html")


class Chart_of_AccountsView(View):
    def get(self, request):
        return render(request, "chart_of_accounts.html")
    




class  Financial_Statements_View(View):
    def get(self, request):
        return render(request, "financial_statements.html")



class TaxexView(View):
    def get(self, request):
        return render(request, "taxes.html")

class Repport_CustomersView(View):
    def get(self, request):
        return render(request, "report_customers.html")
    


class Account_TransactionsView(View):
    def get(self, request):
        return render(request, "account _transactions.html")






class Resetpasswordview(View):
    def get(self, request):
        return render(request, "resetemail.html")

    def post(self,request):
        email = request.POST.get("email")

        user = User.objects.filter(email=email).first()

        if user:
            token = uuid.uuid4()
            obj, _ = EmailToken.objects.get_or_create(user=user)
            obj.email_token = token
            obj.save()
            receiver_email = obj.user.email
            # Sendresetpasswordlink(receiver_email,obj.email_token )
            messages.success(request,f"The link to reset your password has been emailed to: {receiver_email}")
            return render(request, 'resetemail.html')
        
        messages.error(request,f"User does not exist")
        return render(request, 'resetemail.html')

    
class confirmpassword(View):
    def get(self, request, token=None):
        try:
            token_obj = EmailToken.objects.filter(email_token=token).first()

            return render(request, "confirmpassword.html",{'token':token_obj.email_token})
        
        except Exception as e:
            messages.error(request,f"Invaild or expired URL")
            return render(request, 'resetemail.html')
            # return HttpResponse("invaild url")

    def post(self, request,token=None):

        password = request.POST.get("password1")
        confirmpassword = request.POST.get("password2")
        if password != confirmpassword :
            messages.error(request,f"Passwords do not match")
            return render(request, "confirmpassword.html",{'token':token})
        obj  = EmailToken.objects.filter(email_token= token).first()
        try:
            user_obj = User.objects.filter(email=obj.user).first()
            user_obj.set_password(password)
            user_obj.save()
            obj.delete()
            messages.success(request,f"Password updated successfully")
            # return HttpResponse("Passoword  Update  successfully")
            return render(request, "confirmpassword.html",{'token':token})
        except Exception as e:
            messages.error(request,f"User does not exist")
            return render(request, "confirmpassword.html",{'token':token})



def ForgotPasswordPage(request):
    return render(request, 'auth-forgot-password-basic.html')

























