from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('deposit', 'Deposit'),
        ('withdraw', 'Withdraw'),
        ('transfer', 'Transfer'),
    ]

    from_user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name='sent_transactions'
    )
    to_user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name='received_transactions'
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(
        max_length=10, choices=TRANSACTION_TYPES, default='deposit'
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        from_user = self.from_user.username if self.from_user else "N/A"
        to_user = self.to_user.username if self.to_user else "N/A"
        return f"{self.transaction_type.capitalize()} - {self.amount} by {from_user} to {to_user} at {self.timestamp}"
