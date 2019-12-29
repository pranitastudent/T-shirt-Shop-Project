from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings

PRODUCT_CHOICES = (
    ('Womens Red-Tshirt','Womens Red-Tshirt'),
    ('Womens Pink-Tshirt','Womens Pink-Tshirt'),
    ('Womens White-Tshirt','Womens White-Tshirt'),
    ('Mens Black-Tshirt','Mens Black-Tshirt'),
    ('Mens White-Tshirt', 'Mens White-Tshirt'),
    ('Mens Striped-Tshirt','Mens Striped-Tshirt'),
    ('Boy Tshirt', 'Boy Tshirt'),
    ('Girl Unicorn-Tshirt','Girl Unicorn-Tshirt'),   
     
)

# Rating's range adapated from Django star - stackoverflow https://stackoverflow.com/questions/55448221/convert-ratings-in-stars-in-django-template

RATING_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5')
)

class Feedback(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product_name= models.CharField(max_length=100,choices=PRODUCT_CHOICES, null=False, blank=False)
    user_feedback = models.TextField(null=True)
    published_date = models.DateTimeField(auto_now_add=True, null=True)
    ratings = models.CharField(max_length=100,choices=RATING_CHOICES, null=False, blank=False)
    
    def __str__(self):
        return self.product_name
