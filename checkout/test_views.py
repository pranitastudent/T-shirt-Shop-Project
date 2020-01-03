from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User



class TestCheckoutView(TestCase):
    
    def test_checkout_page(self):
        response = self.client.get('/checkout/checkout/')
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')