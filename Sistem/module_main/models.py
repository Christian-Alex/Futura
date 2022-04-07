import os

from django.core.exceptions import ValidationError

from django.db import models
from datetime import datetime

# Create your models here.
def valid_extension(value):
    if (not value.name.endswith('.png') and
        not value.name.endswith('.jpeg') and 
        not value.name.endswith('.jpg')):
        raise ValidationError("Archivos permitidos: .jpg, .jpeg, .png")

def get_date_current():
    return datetime.today().strftime('%d/%m/%Y')

def rol_for_default():
    return {'USER'}

# Entidades 
class Document(models.Model):
    documentId = models.AutoField(primary_key= True, null= False)
    documentName = models.CharField(max_length= 30, null= False, unique= True)
    documentLength = models.CharField(max_length= 50, default= 0)

class Client(models.Model):
    userId = models.AutoField(primary_key= True, null= False)
    fullName = models.CharField(max_length= 50, null= False)
    rules = models.JSONField(default= rol_for_default)
    typeDoc = models.ForeignKey(Document, on_delete=models.CASCADE)
    numDoc = models.CharField(max_length= 20, null= False, unique= True)
    phoneNumber = models.CharField(max_length= 12, null= False)
    email = models.EmailField(max_length = 200)
    password = models.CharField(max_length= 50, null= False)
    dateBirth = models.DateField()
    address = models.CharField(max_length= 300, null= False)
    debitCard = models.CharField(max_length= 20, null= False)
    dateRegister = models.DateField(default= get_date_current)
    active = models.CharField(max_length= 1, default= "1")

class Delivery(models.Model):
    deliveryId = models.AutoField(primary_key= True, null= False)
    deliveryName = models.CharField(max_length= 50, null= False)
    typeDoc = models.ForeignKey(Document, on_delete=models.CASCADE)
    document = models.CharField(max_length= 20, null= False, unique= True)
    dateBirth = models.DateField()
    phoneNumber = models.CharField(max_length= 12, null= False, unique= True)
    active = models.CharField(max_length= 1, default= "1")

###############################################################################

class Categorie(models.Model):
    categorieId = models.AutoField(primary_key= True, null= False)
    categorieName = models.CharField(max_length= 40, null= False, unique= True)

class Product(models.Model):
    prodId = models.AutoField(primary_key= True, null= False)
    prodName = models.CharField(max_length= 50, null= False)
    description = models.CharField(max_length= 300)
    mark = models.CharField(max_length= 50, null= False)
    categories = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    nameImg = models.FileField(max_length= 400, validators=[valid_extension])
    stock = models.IntegerField(default= 0, null= False)
    price = models.DecimalField(default= 0, max_digits= 10, decimal_places= 2)
    valued = models.IntegerField(default= 0, null= False)
    warranty = models.IntegerField(default= 0, null= False)
    
###############################################################################

class Invoce(models.Model):
    invoceId = models.AutoField(primary_key= True)
    userId = models.ForeignKey(Client, on_delete=models.CASCADE)
    prodContent = models.OneToOneField(Product, on_delete=models.CASCADE)
    priceAll = models.DecimalField(max_digits= 10, decimal_places= 2)
    date = models.DateField(default= get_date_current)
    priceDistribution = models.DecimalField(max_digits= 10, decimal_places= 2)

class Order(models.Model):
    orderId = models.AutoField(primary_key= True, null= False)
    deliverId = models.ForeignKey(Delivery, on_delete= models.CASCADE)
    invoId = models.ForeignKey(Invoce, on_delete= models.CASCADE)
    date = models.CharField(default= "00:00", max_length= 5, null= True)
    state = models.IntegerField(default= 0, null= True)
