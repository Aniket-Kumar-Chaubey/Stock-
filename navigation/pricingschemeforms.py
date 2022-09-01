from django.forms import ModelForm
from .models import pricingscheme

class pricingshemeForm(ModelForm):
    class Meta:
        model = pricingscheme
        fields = ('pricingscheme', 'lowerlimit', 'uperlimit', 'purchaseprice', 'profit','profitmarginfactor','salseprice',)



# pricingscheme=models.CharField(max_length=20)
#     lowerlimit=models.DecimalField(max_digits=8,decimal_places=2)
#     uperlimit=models.DecimalField(max_digits=8,decimal_places=2)
#     purchaseprice=models.DecimalField(max_digits=8,decimal_places=2)
#     profitmarginfactor=models.DecimalField(max_digits=8,decimal_places=3)
#     salseprice=models.DecimalField(max_digits=8,decimal_places=2)        