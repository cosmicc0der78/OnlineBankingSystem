# accounts/models.py
from django.db import models
from django.contrib.auth.models import User
import random

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    account_number = models.CharField(max_length=12, unique=True, null=True, blank=True)  # Account number field

    def generate_account_number(self):
        # A simple random number generator for the account number
        return ''.join([str(random.randint(0, 9)) for _ in range(12)])

    def save(self, *args, **kwargs):
        if not self.account_number:
            self.account_number = self.generate_account_number()  # Set account number on save
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username}'s Profile"