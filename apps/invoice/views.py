from django.shortcuts import render
from django.views import View
# Create your views here.


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


