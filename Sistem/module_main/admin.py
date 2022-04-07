from ast import Or
from django.contrib import admin

from .models import *

# Register your models here
admin.site.register(Document)
admin.site.register(Categorie)

admin.site.register(Client)
admin.site.register(Delivery)
admin.site.register(Product)

admin.site.register(Invoce)
admin.site.register(Order)
