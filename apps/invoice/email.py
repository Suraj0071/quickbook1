from email import message
from django.core.mail import send_mail
import random
from . models import *

from django.conf  import settings

def send_otp_email(email):
    try:
        subject = 'Your account Varification mail'
        otp = random.randint(1000,20000)
        message = f'your Otp is {otp}'  
        email_from = settings.EMAIL_HOST
        send_mail(subject, message, email_from, [email])
    except Exception as e:
        print(e)

