from django.apps import apps
from django.test import TestCase
from .apps import FeedbackConfig

class TestAppsConfig(TestCase):
    
    def test_feedback_app(self):
        self.assertEqual("feedback", FeedbackConfig.name)
        self.assertEqual("feedback", apps.get_app_config("feedback").name)