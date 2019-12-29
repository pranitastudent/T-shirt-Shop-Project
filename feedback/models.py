from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings



class Feedback(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product_name= models.CharField(max_length=100, null=True)
    user_feedback = models.TextField(null=True)
    published_date = models.DateTimeField(auto_now_add=True, null=True)
    ratings = models.IntegerField()
    
    def __str__(self):
        return self.product_name
