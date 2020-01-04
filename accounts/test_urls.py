from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import logout,login,register

class TestUrls(SimpleTestCase):
      
  # PLEASE NOTE ALL URLS TESTS WERE CODED FO USING - Django Testing Tutorial - How to set up tests and Testing (https://www.youtube.com/watch?v=0MrgsYswT1c) 
  # The Dumbfounds.
      
    # Login  
    
    def test_login_url_resolves(self):
      url = reverse('login')
      print(resolve(url))
      self.assertEquals(resolve(url).func,login)
      
    # Logout  
      
    def test_logout_url_resolves(self):
      url = reverse('logout')
      print(resolve(url))
      self.assertEquals(resolve(url).func,logout) 
      
    # Register
    
    def test_register_url_resolves(self):
      url = reverse('register')
      print(resolve(url))
      self.assertEquals(resolve(url).func,register)    
      
   