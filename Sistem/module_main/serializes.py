from dataclasses import fields
from rest_framework import serializers

from .models import *

class CategoriesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ('categorieId','categorieName')
    
class DocumentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('documentId','documentName','documentLength')

class ClientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('userId','fullName','rules','typeDoc','numDoc','phoneNumber','email','password','dateBirth','address','debitCard','dateRegister','active')

class DeliverySerializers(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = ('deliveryId','deliveryName','typeDoc','document','dateBirth','phoneNumber','active')

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('prodId','prodName','nameImg','description','mark','categories','stock','price','valued','warranty')

class InvoceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Invoce
        fields = ('invoceId','userId','prodContent','priceAll','date','priceDistribution')

class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('orderId','deliverId','invoId','date','state')

class ForLogin(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('email','password')