from apps.bills.models import Bills_item

from django.db.utils import IntegrityError
from enum import Enum

def bill_items(product, expence, description, quantity, price, tax,obj):
    print("This is taxz =--",tax)
    all_total = 0
    id_obj = obj.id
    for p, e, d, q, pr, t in zip(product, expence, description, quantity, price, tax):   
        print(id_obj)      
        try:
           
            print("Quantity:", q)
            print("Price:", pr)
            print("Tax:", t)
            
            obj = Bills_item.objects.create(product_id=p, expence_id=e, description=d, quantity=str(q), price=str(pr), tax_id=t,
                                            bills_id=id_obj)
            total = int(q)* int(pr)

            if  t == None:
                print("Tax is there ")

            else:
                print("--------------------No tax--")
            all_total = all_total+total
            
            print("--------------------------------",)
        except IntegrityError as e:
            print(f"IntegrityError: {e}")
        except Exception as e:
            print(f"Error: {e}")

class PaymentMothod(Enum):
    Bank_payment = "Bank payment"
    Cash         = "Cash"
    Cheque         = "Cheque"
    Credit_card   = "Credit_card"
    PayPal         = "PayPal"
    Others         = "Others"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)