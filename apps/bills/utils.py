from apps.bills.models import Bills_item
from apps.invoice.models import Tax

from django.db.utils import IntegrityError
from enum import Enum

def bill_items(product, expence, description, quantity, price, tax,obj):
    try:
        print("This is taxz =--",tax)
        all_total = 0
        id_obj = obj.id
        for p, e, d, q, pr, t in zip(product, expence, description, quantity, price, tax):   
            print(id_obj)      
            try:
                items_obj = Bills_item.objects.create(product_id=p, expence_id=e, description=d, quantity=str(q), price=str(pr), tax_id=t,
                                                bills_id=id_obj)
                total = int(q)* int(pr)
                if  t == "":
                    all_total = all_total+total
                else:
                    tax_obj = Tax.objects.get(id=int(t))
                    tax = total * (int(tax_obj.tax_rate) / 100)                 
                    amount = total+tax             
                    all_total = all_total+ amount
        
            except Exception as e:
                print(f"Error: {e}")
        return all_total

    except Exception as e:
        print(f"Error: {e}")

    






# class PaymentMothod(Enum):
#     Bank_payment = "Bank payment"
#     Cash         = "Cash"
#     Cheque         = "Cheque"
#     Credit_card   = "Credit_card"
#     PayPal         = "PayPal"
#     Others         = "Others"

#     @classmethod
#     def choices(cls):
#         return tuple((i.name, i.value) for i in cls)