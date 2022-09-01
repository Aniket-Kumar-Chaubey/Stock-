from django.forms import ModelForm
from .models import customer

class customerForm(ModelForm):
    class Meta:
        model = customer
        fields = ('cust_name', 'cust_ad', 'country', 'state', 'district', 'city', 'pin', 'gstn', 'pan', 'contact',)