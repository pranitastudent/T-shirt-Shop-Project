from django.apps import apps
from django.test import TestCase
from .apps import AccountsConfig

class TestAppsConfig(TestCase):
    
    def test_accounts_app(self):
        self.assertEqual("accounts", AccountsConfig.name)
        self.assertEqual("accounts", apps.get_app_config("accounts").name)