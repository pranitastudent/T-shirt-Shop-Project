from django import forms
from .models import Feedback


# Create a feedback from so user can give feedback and rating


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = {'product_name', 'user_feedback', 'rating'}
        widgets= {
            'user_feedback':forms.Textarea(attrs={
                "rows":5,
                "placeholder":"Please add your feedback here"
                })
            }