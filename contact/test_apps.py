from django.apps import apps
from django.test import TestCase
from .apps import ContactConfig

class TestAppsConfig(TestCase):
    
    def test_contact_app(self):
        self.assertEqual("contact", ContactConfig.name)
        self.assertEqual("contact", apps.get_app_config("contact").name)