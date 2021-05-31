from django.db import models

# Create your models here.

class Bank(models.Model):
    bank_id = models.IntegerField(default=0)
    bank_name = models.CharField(max_length=50, default='')
    ifsc_code = models.CharField(max_length=20,default='')
    Branch = models.CharField(max_length=30,default='')
    city = models.CharField(max_length=10,default='')
    address = models.CharField(max_length=1000,default='')
    District = models.CharField(max_length=30, default='')
    State = models.CharField(max_length=2000,default='')

    
# 