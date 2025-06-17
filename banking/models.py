# banking/models.py
from django.db import models
from django.contrib.auth.models import User
from transactions.models import Transaction  # Ensure this model exists as per your design

class Account(models.Model):
    ACCOUNT_TYPES = [
        ('savings', 'Savings'),
        ('checking', 'Checking'),
        ('business', 'Business'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPES, default='savings')

    def __str__(self):
        return f'{self.user.username} - {self.account_type.capitalize()} Account'

    def deposit(self, amount):
        """Deposit money into the account and log it as a transaction."""
        if amount > 0:
            self.balance += amount
            self.save()
            # Log the deposit transaction
            Transaction.objects.create(
                to_user=self.user,  # The user who owns this account is the recipient
                amount=amount,
                transaction_type='deposit'
            )

    def withdraw(self, amount):
        """Withdraw money from the account and log it as a transaction."""
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            self.save()
            # Log the withdrawal transaction
            Transaction.objects.create(
                from_user=self.user,  # The user who owns this account is the sender
                amount=amount,
                transaction_type='withdraw'
            )
            return True
        return False
