from django.db import models
from django.forms import ModelForm
from .models import salseinvoice

class salseForm(ModelForm):
    class Meta:
        model=salseinvoice
        fields = ( 
        'invoicedate',  
        'custmercode', 'customeraddress','customergstin',
        'itemcode','desc','uom','quantity','unitprice','amount',
        'batchno','cgst','igst','sgst','cgstamount',
        'igstamount','sgstamount','totalamount')




# invoiceno=models.CharField(max_length=100000,blank=True)
#     =models.DateField()
#     invoiceref=models.CharField(max_length=30)
#     = models.CharField(max_length=100000,blank=True)
#     #vname = models.CharField(max_length=122)
#     = models.CharField(max_length=122)
#     =models.CharField(max_length=30,blank=True)
#     itemcode=models.CharField(max_length=30,blank=True)
#     desc = models.CharField(max_length=122)
#     uom = models.CharField(max_length=122)
#     quantity=models.DecimalField(max_digits=5,decimal_places=2)
#     unitprice=models.DecimalField(max_digits=5,decimal_places=2)
#     amount=models.DecimalField(max_digits=5,decimal_places=2)
#     batchno=models.CharField(max_length=100000)
#     cgst=models.DecimalField(max_digits=5,decimal_places=2)
#     igst=models.DecimalField(max_digits=5,decimal_places=2)
#     sgst=models.DecimalField(max_digits=5,decimal_places=2)
#     cgstamount=models.DecimalField(max_digits=9,decimal_places=2)
#     sgstamount=models.DecimalField(max_digits=9,decimal_places=2)
#     igstamount=models.DecimalField(max_digits=9,decimal_places=2)
#     totalamount=models.DecimalField(max_digits=9,decimal_places=2)        