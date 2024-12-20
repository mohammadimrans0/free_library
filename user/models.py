from django.db import models
from django.contrib.auth.models import User


class UserAccount(models.Model):
    user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE)
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.user.first_name}'s account"
    

class Deposit(models.Model):
    user_account = models.ForeignKey(UserAccount, related_name='deposits', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Deposit of ${self.amount} to {self.user_account.user.username}"