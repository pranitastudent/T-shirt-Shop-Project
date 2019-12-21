from django import forms
from ckeditor_uploader.fields import RichTextUploadingField


# Contact Form- Code adapted from (Django-2.2 Part-7 Django Contact Form with SMTP Email Backed Tutorial | By Creative web) 

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True, widget=forms.Textarea(attrs={
        "placeholder":" Full name",
        "rows":1,
    }))
    contact_email = forms.EmailField(required=True, widget=forms.Textarea(attrs={
        "placeholder":"Email Address",
        'rows': 1, 
        }))
    
    content = RichTextUploadingField(widget=forms.Select(attrs={
        'required': True,
        "placeholder":"Message",
        'rows': 1, 
        }))
   
    
    