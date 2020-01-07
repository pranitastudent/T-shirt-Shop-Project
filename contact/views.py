import urllib
import json
from django.shortcuts import render
from django.contrib import  messages
from django.core.mail import EmailMessage
from django.template.loader import get_template
from .forms import ContactForm
from django.conf import settings


# Contact Form- Code adapted from (Django-2.2 Part-7 Django Contact Form with SMTP Email Backed Tutorial | By Creative web) 

# POST method initiated for Contact

def contact(request):
    Contact_Form = ContactForm
    if request.method == 'POST':
        form = Contact_Form(data=request.POST)
        
# Check is Contact form is valid

        if form.is_valid():
            contact_name = request.POST.get('contact_name')
            contact_email = request.POST.get('contact_email')
            contact_content = request.POST.get('content')
            
# Contact form message template

            template = get_template('contact/contact_form.txt')
            context = {
                'contact_name' : contact_name,
                'contact_email' : contact_email,
                'contact_content' : contact_content,
            }
            
            content = template.render(context)
            
# Format of received email message

            email = EmailMessage(
                "New contact form email",
                content,
                "Pranita's T-shirt Shop" + '',
                ['pranitacoder12@gmail.com'],
                headers = { 'Reply To': contact_email }
            )
            
# End of adapted code
            
            # reCaptcha - CODE TAKEN FROM How to Add reCAPTCHA to a Django Site- VITOR FREITAS
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            ''' End reCAPTCHA validation '''
            
            email.send()

            if result['success']:
                messages.success(request, "You email has been successfully sent!") 
            else:
                messages.error(request, "Your reCAPTCHA is invalid, please try again")    
            # End of taken code
            return render (request, 'home/index.html')
        else:
            messages.error(request, "Please check your email is correct")
            print(form.errors)      

    return render(request, 'contact/contact.html', {'contact_form':Contact_Form })

