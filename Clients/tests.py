from django.test import TestCase, Client
from django.urls import reverse

class ClientTests(TestCase):

    def setUp(self):
        self.client = Client()
    
    def test_dashboard(self):
        get = self.client.get(reverse('dashboard'))
        self.assertEqual(get.status_code, 200)