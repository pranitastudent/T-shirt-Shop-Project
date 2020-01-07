from django.apps import apps
from django.test import TestCase
from home.apps import HomeConfig


class TestAppsConfig(TestCase):

    def test_home_app(self):
        self.assertEqual("home", HomeConfig.name)
        self.assertEqual("home", apps.get_app_config("home").name)
