from django.contrib import admin
from navigation.models import item
from navigation.models import vendor
from navigation.models import customer

# Register your models here.
admin.site.register(item)
admin.site.register(vendor)
admin.site.register(customer)
