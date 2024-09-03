from django.db import models
import sys

print(sys.path)
from members.models import UserDetails


# Create your models here.

class ReraComplaints(models.Model):
    flat_no = models.ForeignKey(UserDetails, on_delete=models.PROTECT)
    date_of_refund_file = models.DateTimeField(blank=False)
    date_of_refund_order_execution = models.DateTimeField(blank=True)
    date_of_joining_association = models.DateTimeField(blank=False)
    bank_emi_stop_date = models.DateTimeField(blank=True)
    doc_image = models.FileField(upload_to='files')


class BankDetails(models.Model):
    flat_no = models.ForeignKey(UserDetails, on_delete=models.PROTECT)
    bank_name = models.CharField(max_length=30)
    loan_amount = models.IntegerField(max_length=10)
    amount_processed = models.IntegerField(max_length=10)
    amount_pending = models.IntegerField(max_length=10)
    emi_status = models.BooleanField()
    loan_status = models.BooleanField()
