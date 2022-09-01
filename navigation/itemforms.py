from django.forms import ModelForm
from .models import item

class itemForm(ModelForm):
    class Meta:
        model = item
        fields = ('itemcode','desc', 'uom', 'manufac', 'pscheme','puchaseprice',)