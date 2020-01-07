from django import forms
from .models import Feedback
from django.forms import widgets


# Create a feedback from so user can give feedback and rating


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = {'product_name', 'ratings', 'user_feedback'}
