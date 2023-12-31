from django.contrib import admin
from django.urls import path
from apps.bills import views


urlpatterns = [
    path("bills/", views.BillsView.as_view(), name="bills"),
    path("create-bill/", views.CreateBill.as_view(), name="create-bill"),
    path("edit-bill/<int:id>/", views.EditBill.as_view(), name="edit-bill"),
    path("delete-bill/<int:id>/", views.bill_delete, name="delete-bill"),
    path("payed-bill/<int:id>/", views.PaidBill.as_view(), name="payed-bill"),


  

    path("vendors/", views.VendorsView.as_view(), name="vendors"),
    path("add-vendors/", views.VendorCreate.as_view(), name="add-vendors"),
    path("ediit-vendors/<int:id>/", views.VendorEdit.as_view(), name="edit-vendors"),
    path("delete-vendors/<int:id>/", views.vendor_delete, name="delete-vendors"),
    path("upload-vendors/", views.   upload_vendor_csv, name="upload-vendors"),
    

]