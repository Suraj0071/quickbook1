from django.template.loader import get_template
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
import os
from apps.invoice.models import Item ,Tax


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)#, link_callback=fetch_resources)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


def save_item(itemname,quantity,price,tax,customer,invoice):
    try:
        all_total = 0
        amount = []
        amount_paid = 0
        tax_list = []

        for item_name ,item_qty,item_price,t in zip(itemname,quantity,price,tax):
            # amount_save = int(item_qty) * int(item_price)
            total = int(item_qty)* int(item_price)
            
            
            # amount.append(amount_save)

            # alltotal= amount_save+alltotal
            Item.objects.create(invoice = invoice,name=item_name, quantity=int(item_qty),price=int(item_price),amount=total , customer=customer)
            
            if  t == "":
                amount.append(total)
                all_total = all_total + total
                tax_list.append("No tax")
            else:
                tax_obj = Tax.objects.get(id=int(t))
                tax_price = total * (int(tax_obj.tax_rate) / 100)                 
                tax_amount = total + tax_price             
                amount.append(tax_amount)
                tax_list.append(f"{tax_obj.tax_rate}%")

                all_total = all_total + tax_amount



        
        # print(alltotal)
        # tax = int(alltotal * (5 / 100))
        # amount_paid = alltotal+tax
        # print(alltotal , amount_paid)


        print("++++++++++++++++++++++",all_total,amount)

    
        price_data = {
            "amount" : amount,
            "alltotal" :all_total,
            "tax_list" :tax_list
            # "all_total"  : all_total
            
        }

        return price_data
    except Exception as e:
        print(e)


# total = int(q)* int(pr)
#                 if  t == "":
#                     all_total = all_total+total
#                 else:
#                     tax_obj = Tax.objects.get(id=int(t))
#                     tax = total * (int(tax_obj.tax_rate) / 100)                 
#                     amount = total+tax             
#                     all_total = all_total+ amount