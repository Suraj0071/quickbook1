from django.contrib import admin
from django.urls import path
from app1 import views


urlpatterns = [path('',views.LoginPage,name='login'),
    path('auth-register-basic/',views.SignupPage,name='signup'),
    path('logout/',views.LogoutPage,name='logout'),
    path('index/', views.IndexPage, name='index'),
    path('profile/', views.profile, name='profile'),
    path('home-admin/', views.adminhome, name='admin_home'),
    path("uploadfile/",views.uploadfile , name="uploadfile"),
    path("show-files-data/",views.showfilesdata , name="showfilesdate"),

    path('auth-forgot-password-basic.html/', views.ForgotPasswordPage, name='forgot_password')

]