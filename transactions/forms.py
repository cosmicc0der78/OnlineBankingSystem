# transactions/forms.py

from django import forms
from django.contrib.auth.models import User

class TransferForm(forms.Form):
    to_account = forms.ModelChoiceField(queryset=User.objects.all(), label="Recipient")
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
