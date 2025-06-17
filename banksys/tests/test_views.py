from django.test import TestCase
from django.urls import reverse
from accounts.models import User

class ViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testviewuser', password='password')
    
    def test_home_page_access(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_profile_update_access(self):
        self.client.login(username='testviewuser', password='password')
        response = self.client.get(reverse('profile_update'))
        self.assertEqual(response.status_code, 200)

    def test_login_page_access(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
