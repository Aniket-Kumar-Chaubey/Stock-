from django.forms import ModelForm
from .models import purchesinvoice

class purchesForm(ModelForm):
    class Meta:
        model = purchesinvoice
        fields = ( 
        'invoicedate',
        'vcode', 'vname','vadd','vengstin',
        'itemcode','desc','uom','quantity','unitprice','amount','cgst','igst','sgst','cgstamount','igstamount','sgstamount','totalamount')


