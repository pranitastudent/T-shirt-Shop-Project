from django.apps import apps
from django.test import TestCase
from cart.apps import CartConfig

class TestAccountsConfig(TestCase):
    
    def test_cart_app(self):
        self.assertEqual("cart", CartConfig.name)
        self.assertEqual("cart", apps.get_app_config("cart").name)