from django.test import SimpleTestCase
from django.urls import reverse, resolve
from checkout.views import checkout


class TestUrls(SimpleTestCase):
    # Checkout Url Test

    def test_checkout_url_resolves(self):
        url = reverse('checkout')
        print(resolve(url))
        self.assertEquals(resolve(url).func, checkout)
