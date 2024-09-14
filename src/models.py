from django.db import models
from django.contrib.auth.models import User

# Interest From Lending Money : Models
# Borrower Model
class Borrower(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    borrower_name = models.CharField(max_length=250)
    amount_lent = models.IntegerField()
    date_lent = models.DateField(auto_now=False,auto_now_add=False)
    interest = models.DecimalField(max_digits=100,decimal_places=2)
    total_amount_to_be_paid = models.DecimalField(max_digits=1000,decimal_places=2)

    def __str__(self):
        return self.borrower_name
    
# Business : Models
# Farmer Model
class Farmer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    farmer_name = models.CharField(max_length=250)
    farmer_cost = models.IntegerField()
    labour_expenses = models.IntegerField()
    vehicle_expenses = models.IntegerField()
    other_expenses = models.IntegerField()
    patti = models.IntegerField()
    total_profit_or_loss = models.IntegerField()

    def __str__(self):
        return self.farmer_name

# Agriculture : Models
# Crop Model
class Crop(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    crop_name = models.CharField(max_length=250)
    investment = models.IntegerField()
    pesticides_expenses = models.IntegerField()
    labour_expenses = models.IntegerField()
    other_expenses = models.IntegerField()
    income = models.IntegerField()
    present_profit_or_loss = models.IntegerField()

    def __str__(self):
        return self.crop_name

# Saving Expense : Model
# SavingExpense MODEL
class SavingExpense(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    type = models.CharField(max_length=10)
    purpose = models.CharField(max_length=250)
    amount = models.IntegerField()

    def __str__(self):
        return self.purpose
# Usernetworth Model
class Networth(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    total_savings = models.IntegerField()
    total_expenses = models.IntegerField()
    net_worth = models.IntegerField()

    def __str__(self):
        return self.user.username

