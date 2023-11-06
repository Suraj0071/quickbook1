from django.contrib import admin
from django.urls import path
from apps.bills import views


urlpatterns = [
    path("bills/", views.BillsView.as_view(), name="bills"),
    path("create-bill/", views.CreateBill.as_view(), name="create-bill"),
    path("edit-bill/", views.EditBill.as_view(), name="edit-bill"),
]