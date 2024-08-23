from django.db import models
from phone_field import PhoneField


# Create your models here.

class UserDetails(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100, primary_key=True)
    phone_number = PhoneField(blank=False, primary_key=True, help_text='Contact phone number')
    alternate_number = PhoneField(blank=True, help_text='Alternate Contact phone number')
    flat_no = models.CharField(max_length=20, primary_key=True)


class TransactionDetails(models.Model):
    flat_no = models.ForeignKey(UserDetails, max_length=20, primary_key=True, on_delete=models.CASCADE() )
    phone_number = PhoneField(blank=False, primary_key=True, help_text='Contact phone number')
    date_of_purchase = models.DateTimeField(blank=False)
    date_of_sale_agreement = models.DateTimeField(blank=False)
    date_of_sale_deed = models.DateTimeField(blank=True)
    date_of_register_sale_agreement = models.DateTimeField(blank=True)
    seller_name = models.TextField(max_length=50)
    seller_type = models.TextField(max_length=50)
    doc_image = models.FileField(upload_to='files')

