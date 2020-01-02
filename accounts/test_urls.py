from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import logout,login,register

class TestUrls(SimpleTestCase):
      
    # Login  
    
    def test_login_url_is_resolved(self):
      url = reverse('login')
      print(resolve(url))
      self.assertEquals(resolve(url).func,login)
      
    # Logout  
      
    def test_logout_url_is_resolved(self):
      url = reverse('logout')
      print(resolve(url))
      self.assertEquals(resolve(url).func,logout) 
      
    # Register
    
    def test_register_url_is_resolved(self):
      url = reverse('register')
      print(resolve(url))
      self.assertEquals(resolve(url).func,register)     