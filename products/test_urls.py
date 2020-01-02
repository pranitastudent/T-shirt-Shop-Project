from django.test import SimpleTestCase
from django.urls import reverse, resolve
from products.views import all_products

class TestUrls(SimpleTestCase):
    # Product Url
    
    def test_products_url_resolves(self):
       url = reverse('products')
       print(resolve(url))
       self.assertEquals(resolve(url).func,all_products)