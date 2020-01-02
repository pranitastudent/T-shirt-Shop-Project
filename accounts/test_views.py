from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from accounts.forms import UserRegistrationForm, UserLoginForm
from home.views import index

class TestAccountsViews(TestCase):
    
    def test_registration_page(self):
        response = self.client.get('/accounts/register/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')
    
    def test_login_page(self):
        response = self.client.get('/accounts/login/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')
        
    # def test_logged_in_page(self):
    #     user = User.objects.create_user(
    #         'test_user',
    #         'test_user@gmail.com'
    #         'example'
    #     )
    #     user.save()
    #     logged_in = self.client.login(username='test_user', password='example')
    #     response = self.client.get('/home/index/')
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'home/index.html')    
    
   
            
        
        