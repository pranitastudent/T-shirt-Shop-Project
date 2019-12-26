from django.db import models
from datetime import datetime

# Create your models here.

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Girl', 'Girl'),
    ('Boy', 'Boy')
)


class Product(models.Model):
    product_name = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=3,decimal_places=2)
    image = models.ImageField(upload_to='images')
    category = models.TextField(choices=GENDER_CHOICES)
    product_date = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.product_name
   
    
    
    