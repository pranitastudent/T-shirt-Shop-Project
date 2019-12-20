from django.db import models

# Create your models here.

SIZE_CHOICES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('XL', 'XLarge')
)

COLOR_CHOICES = (
    ('Red', 'Red'),
    ('Green', 'Green'),
    ('Black', 'Black'),
    ('White', 'White')
)
class Product(models.Model):
    product_name = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=3,decimal_places=2)
    image = models.ImageField(upload_to='images')
    category = models.CharField(choices=SIZE_CHOICES, max_length=1)
    size = models.CharField(choices=COLOR_CHOICES, max_length=1)
    
    
    