from django.test import TestCase, Client
from django.urls import reverse
import random
from .models import EmailVerification
from django.contrib.auth.models import User
from Clients.models import Client as cl

test_client = {
    'first_name': 'Elijah',
    'last_name': 'Mukisa',
    'email': "mukisaelijah293@gmail.com",
    'password': "14qw@",
    'confirmpassword': "14qw@",
    'code': str(random.randint(1111, 9999))
}

class ClientTests(TestCase):

    def setUp(self):
        self.client = Client()


    def test_signup(self):
        get = self.client.get(reverse('signup'))
        self.assertEqual(get.status_code, 200)
        post = self.client.post(reverse('send-email-verification'), {'email': test_client['email']})
        self.assertEqual(post.status_code, 200)
        verification = EmailVerification.objects.get(email=test_client['email'])
        test_client['code'] = verification.code
        post = self.client.post(reverse('signup'), test_client)
        self.assertEqual(post.status_code, 302)
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1)
        client_count = cl.objects.all().count()
        self.assertEqual(client_count, 1)

    
    def test_login(self):
        get = self.client.get(reverse('login'))
        self.assertEqual(get.status_code, 200)
        post = self.client.post(reverse('login'), {"email": test_client['email'], "password": test_client['password']})
        self.assertEqual(post.status_code, 302)

    def test_resetpassword(self):
        pass