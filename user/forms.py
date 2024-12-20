from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Deposit, UserAccount


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        # Save the User instance
        our_user = super().save(commit=commit)

        # Create UserAccount only if the user instance was saved
        if commit:
            UserAccount.objects.get_or_create(user=our_user)

        return our_user


from django import forms
from .models import Deposit

class DepositForm(forms.ModelForm):
    class Meta:
        model = Deposit
        fields = ['amount']

    def __init__(self, *args, **kwargs):
        self.account = kwargs.pop('account', None)
        super().__init__(*args, **kwargs)

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount <= 0:
            raise forms.ValidationError("Deposit amount must be greater than zero.")
        return amount

    def save(self, commit=True):
        if not self.account:
            raise ValueError("Account must be provided to the form.")

        # Create and return the Deposit instance
        deposit = super().save(commit=False)
        deposit.user_account = self.account

        if commit:
            deposit.save()
        return deposit

