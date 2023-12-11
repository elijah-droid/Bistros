from django.test import TestCase, Client
from django.urls import reverse
import random
from django.contrib.auth.models import User
from Clients.models import Client as cl


class BistroTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_homepage(self):
        get = self.client.get(reverse('home'))
        self.assertEqual(get.status_code, 200)

    def test_menu(self):
        get = self.client.get(reverse('menu'))
        self.assertEqual(get.status_code, 200)