from django.forms import ModelForm
from .models import paymentvoucher

class paymentvoucherForm(ModelForm):
    class Meta:
        model = paymentvoucher
        fields = ( 
        'vcode', 'vname','vadd','vengstin',
        'itemcode','desc','uom','quantity','unitprice',
        'amount','cgst','igst','sgst','cgstamount',
        'igstamount','sgstamount','totalamount')


