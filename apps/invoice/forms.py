from django import forms



from . models import *


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

    def clean_email(self):
        email = self.cleaned_data['email']
        print("Thisis email",email)
        