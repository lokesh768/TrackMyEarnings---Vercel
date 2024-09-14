from django.contrib import admin
from .models import Borrower,Farmer, Crop, SavingExpense, Networth

# Register your models here.
admin.site.register(Borrower)
admin.site.register(Farmer)
admin.site.register(Crop)
admin.site.register(SavingExpense)
admin.site.register(Networth)