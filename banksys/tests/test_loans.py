from django.test import TestCase
from django.urls import reverse
from loans.models import Loan
from accounts.models import User

class LoansTestCase(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='loanuser', password='loanpass')
        self.client.login(username='loanuser', password='loanpass')
    
    def test_apply_for_loan(self):
        # Test applying for a loan
        response = self.client.post(reverse('apply_loan'), {'amount': 5000, 'loan_type': 'personal'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Loan.objects.filter(user=self.user, amount=5000, loan_type='personal').exists())
    
    def test_view_loans(self):
        # Test viewing loans
        Loan.objects.create(user=self.user, amount=3000, loan_type='education')
        response = self.client.get(reverse('view_loans'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'education')
