from django.db import models


# Create your models here.

class UserDetails(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    flat_no = models.CharField(max_length=20, primary_key=True)

class EmailID(models.Model):
    flat_no = models.ForeignKey(UserDetails, max_length=20, on_delete=models.PROTECT)
    email = models.EmailField(max_length=100, primary_key=True)
class ContactNumber(models.Model):
    flat_no = models.ForeignKey(UserDetails, max_length=20, on_delete=models.PROTECT)
    phone_number = models.IntegerField(blank=False, primary_key=True)
    alternate_number = models.IntegerField(blank=True)

class TransactionDetails(models.Model):
    flat_no = models.ForeignKey(UserDetails, max_length=20, on_delete=models.PROTECT)
    date_of_purchase = models.DateTimeField(blank=False)
    date_of_sale_agreement = models.DateTimeField(blank=False)
    date_of_sale_deed = models.DateTimeField(blank=True)
    date_of_register_sale_agreement = models.DateTimeField(blank=True)
    seller_name = models.TextField(max_length=50)
    seller_type = models.TextField(max_length=50)

