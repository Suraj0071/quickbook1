from django.contrib import admin
from django.urls import path
from apps.invoice import views

urlpatterns = [
  
    path("invoices/", views.InvoicesView.as_view(), name="invoices"),
    path("customer-statements/", views.Customer_statementsView.as_view(), name="customer-statements"),
    path("customers/", views.CustomersView.as_view(), name="customers"),
    path("products-services/", views.Products_servicesView.as_view(), name="products-services"),
    path("bills/", views.BillsView.as_view(), name="bills"),
    path("vendors/", views.VendorsView.as_view(), name="vendors"),
    path("transactions/", views.TransactionsView.as_view(), name="transactions"),
    
    path("reconciliation/", views.ReconciliationView.as_view(), name="reconciliation"),
    path("chart-of-accounts/", views.Chart_of_AccountsView.as_view(), name="chart-of-accounts"),
    path("financial_statements/", views.Financial_Statements_View.as_view(), name="financial-statements"),
    path("taxex/", views.TaxexView.as_view(), name="taxex"),
    path("repport-customers/", views.Repport_CustomersView.as_view(), name="repport-customers"),
    path("account-transactions/", views.Account_TransactionsView.as_view(), name="account-transactions"),
    path("create_invoice/", views.create_invoice.as_view(), name="create_invoice"),
    # path("add-business/", views.AddBusinessview.as_view(), name="add-business"),





]