from django.forms import ModelForm
from .models import vendor

class vendorForm(ModelForm):
    class Meta:
        model = vendor
        fields = ('vcode', 'vname', 'vadd', 'city', 'pin','state','gstn','pan','contact')
        labels ={'vcode':'Vendor Code','vname':'Vendor Name','vadd':'Vendor Address','city':'City',
                  'pin':'PIN','state':'State','gstn':'GSTIN','pan':'PAN','contact':'Contact'
                
                }