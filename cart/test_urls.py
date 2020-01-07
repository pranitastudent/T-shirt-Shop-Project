from django.test import SimpleTestCase
from django.urls import reverse, resolve
from cart.views import view_cart


class TestUrls(SimpleTestCase):

    # View Cart

    def test_view_cart_url_resolves(self):
        url = reverse('view_cart')
        print(resolve(url))
        self.assertEquals(resolve(url).func, view_cart)
