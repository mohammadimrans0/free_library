from django.contrib import admin

from user.models import UserAccount, Deposit

# Register your models here.
admin.site.register(UserAccount)
admin.site.register(Deposit)