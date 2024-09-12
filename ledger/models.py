from django.db import models
from django.utils import timezone
 
class Staff(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    emp_no=models.IntegerField()
    designation = models.CharField(max_length=64)
    section = models.CharField(max_length=64)
    phone = models.BigIntegerField()
    remark = models.CharField(max_length=150, blank=True)
    balance = models.IntegerField(default=0)
    trash = models.BooleanField(default=False)
    created_on= models.DateField(default=timezone.now)
    def __str__(self):
        return self.name

class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    bill_no = models.CharField(max_length=128, blank=True, null=True)
    date = models.DateField(default=timezone.now)
    advance = models.FloatField(default=0)
    bill_amount = models.FloatField(default=0)
    balance = models.FloatField()
    grand_balance = models.FloatField()
    remark = models.CharField(max_length=128, blank=True, null=True)
    created_on=models.DateField(default=timezone.now)

