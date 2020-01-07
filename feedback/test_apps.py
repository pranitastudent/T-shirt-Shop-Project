from django.apps import apps
from django.test import TestCase
from feedback.apps import FeedbackConfig


class TestAccountsConfig(TestCase):

    def test_feedback_app(self):
        self.assertEqual("feedback", FeedbackConfig.name)
        self.assertEqual("feedback", apps.get_app_config("feedback").name)
