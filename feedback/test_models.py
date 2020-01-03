from django.test import TestCase
from feedback.models import Feedback

class FeedbackTest(TestCase):
    
    def test_feedback_product_name_str_test(self):
        test_feedback = Feedback(product_name="test",
                                 user_feedback="good",
                                 published_date="2020-05-06",
                                 ratings='4',
                                 upvote=1)
        self.assertEqual(str(test_feedback.product_name), "test")
        