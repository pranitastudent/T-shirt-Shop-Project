from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class TestCheckoutView(TestCase):

    # User needs to login in First

    def setUp(self):
        user = User.objects.create_user(
            username='username', password='password')
        self.client.login(username='username', password='password')

    # User then checkout

    def test_checkout_page(self):
        response = self.client.get('/checkout/checkout/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed('checkout.html')
