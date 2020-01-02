from django.test import SimpleTestCase
from django.urls import reverse, resolve
from feedback.views import get_feedback, add_feedback

class TestUrls(SimpleTestCase):
    
    # Feedback Url- Get Feedback
    
      def test_get_feedback_url_resolves(self):
       url = reverse('get_feedback')
       print(resolve(url))
       self.assertEquals(resolve(url).func,get_feedback)
       
    # Feedback Url- Add Feedback
    
      def test_add_feedback_url_resolves(self):
        url = reverse('add_feedback')
        print(resolve(url))
        self.assertEquals(resolve(url).func,add_feedback)
          
          
          
             