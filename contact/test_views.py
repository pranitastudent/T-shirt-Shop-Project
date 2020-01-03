from django.test import TestCase, Client
from django.urls import reverse


class TestContactView(TestCase):
    
    def test_contact_page(self):
        response = self.client.get('/contact/contact/')
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'contact/contact.html')