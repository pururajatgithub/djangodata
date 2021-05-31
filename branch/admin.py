from django.contrib import admin

from .models import Bank
# Register your models here.

class AdminBank(admin.ModelAdmin):
    list_display = ['bank_id', 'bank_name', 'ifsc_code','Branch','city','address','District','State']


admin.site.register(Bank,AdminBank)