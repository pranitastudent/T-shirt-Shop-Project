from django import forms

# Contact Form- Code adapted from (Django-2.2 Part-7 Django Contact Form with SMTP Email Backed Tutorial | By Creative web) 

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True, widget=forms.Textarea(attrs={
        "placeholder":" Please enter your name",
        "rows":1,
    }))
    contact_email = forms.EmailField(required=True, widget=forms.Textarea(attrs={
        "placeholder":"Please enter your email address",
        "rows":1,
    }))
    message = forms.CharField(required = True, widget=forms.Textarea(attrs={
        "rows":5,
        "placeholder":"Please enter your message",
    }))
    
    