from django.test import TestCase
from django.urls import reverse
from accounts.models import User
from django.core import mail

class AccountsTestCase(TestCase):
    
    def setUp(self):
        # Create a user for login tests
        self.user = User.objects.create_user(
            username='testuser', email='test@example.com', password='password123', role='Customer'
        )
    
    def test_registration(self):
        # Test user registration
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'password1': 'newpassword123',
            'password2': 'newpassword123',
            'email': 'newuser@example.com',
            'contact': '1234567890',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='newuser').exists())
    
    def test_login(self):
        # Test user login
        response = self.client.post(reverse('login'), {
            'username': 'lasya',
            'password': 'lasyalasya',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('home'))
    
    def test_profile_update(self):
        # Test profile update functionality
        self.client.login(username='lasya', password='lasyalasya')
        response = self.client.post(reverse('profile_update'), {
            'email': 'updated@example.com',
            'contact': '0987654321',
        })
        self.user.refresh_from_db()
        self.assertEqual(self.user.email, 'updated@example.com')
    
    def test_otp_login(self):
        # Simulate OTP being sent to the user
        otp = '3773'  # Mocked OTP
        with self.settings(EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend'):
            response = self.client.post(reverse('login_with_otp'), {
                'username': 'testuser',
                'password': 'password123',
            })
            self.assertEqual(response.status_code, 302)
            self.assertIn('step', self.client.session)
            self.client.session['otp_sent'] = otp  # Manually set the OTP in the session
            
            # User enters the OTP
            response = self.client.post(reverse('login_with_otp'), {'otp': otp})
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.url, reverse('home'))
