from apps.bills.models import Bills_item

from django.db.utils import IntegrityError

def bill_items(obj ,product, expence, description, quantity, price, tax):
    for p, e, d, q, pr, t in zip(product, expence, description, quantity, price, tax):         
        try:
            obj = Bills_item.objects.create(product_id=p, expence_id=e, description=d, quantity=str(q), price=str(pr), tax_id=t,
                                            bills=obj)
        except IntegrityError as e:
            print(f"IntegrityError: {e}")
        except Exception as e:
            print(f"Error: {e}")


# def bill_items(product, expence, description, quantity, price, tax):
#     for p, e, d, q, pr, t in zip(product, expence, description, quantity, price, tax):         
#         print("Product:", p)
#         print("Expence:", e)
#         print("Description:", d)
#         print("Quantity:", q)
#         print("Price:", pr)
#         print("Tax:", t)
#         obj = Bills_item.objects.create(product_id=p, expence_id=e, description=d, quantity=str(q), price=str(pr), tax_id=t)
        
