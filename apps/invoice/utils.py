from django.template.loader import get_template
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
import os
from apps.invoice.models import Item
def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)#, link_callback=fetch_resources)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


def save_item(itemname,quantity,price,customer):
    alltotal = 0
    amount = []
    
    
    for item_name ,item_qty,item_price in zip(itemname,quantity,price):
        amount_save = int(item_qty) * int(item_price)
        amount.append(amount_save)
        alltotal= amount_save+alltotal
        Item.objects.create(name=item_name, quantity=int(item_qty),price=int(item_price),amount=amount_save , customer=customer)
    # print(alltotal)
    tax = int(alltotal * (5 / 100))
    amount_paid = alltotal+tax
    print(alltotal , amount_paid)

 
    price_data = {
        "amount" : amount,
        "alltotal" :alltotal,
        "amount_paid"  : amount_paid
        
    }

    return price_data