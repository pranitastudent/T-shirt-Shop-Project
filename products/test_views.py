from django.test import TestCase, Client
from django.urls import reverse


class TestProductsView(TestCase):
    
    def test_products_page(self):
        response = self.client.get('/products/products/')
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'products/products.html')

      