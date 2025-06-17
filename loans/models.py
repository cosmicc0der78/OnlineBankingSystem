from django.db import models
from django.contrib.auth.models import User

class LoanApplication(models.Model):
    LOAN_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    loan_amount = models.DecimalField(max_digits=12, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    loan_term = models.IntegerField(help_text="Loan term in months")
    status = models.CharField(max_length=10, choices=LOAN_STATUS_CHOICES, default='pending')
    date_submitted = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Loan Application from {self.user.username} - {self.status}"

    def calculate_total_repayment(self):
        """Simple formula to calculate total repayment amount including interest."""
        return self.loan_amount * (1 + (self.interest_rate / 100) * self.loan_term)
