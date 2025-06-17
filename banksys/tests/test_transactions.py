from django.test import TestCase
from django.urls import reverse
from transactions.models import Transaction
from accounts.models import User

class TransactionsTestCase(TestCase):
    
    def setUp(self):
        # Create a user for transaction tests
        self.user = User.objects.create_user(username='transactionuser', password='transactionpass')
        self.client.login(username='transactionuser', password='transactionpass')
    
    def test_deposit(self):
        # Test deposit functionality
        response = self.client.post(reverse('deposit'), {'amount': 1000})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Transaction.objects.filter(user=self.user, amount=1000).exists())
    
    def test_withdraw(self):
        # Test withdraw functionality
        self.client.post(reverse('deposit'), {'amount': 2000})
        response = self.client.post(reverse('withdraw'), {'amount': 500})
        self.assertEqual(response.status_code, 302)
        transaction = Transaction.objects.filter(user=self.user, transaction_type='withdraw').first()
        self.assertIsNotNone(transaction)
        self.assertEqual(transaction.amount, 500)
