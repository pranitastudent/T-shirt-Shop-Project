from django.shortcuts import render, render_to_response 
from django.contrib import  messages
from django.core.mail import EmailMessage
from django.template.loader import get_template
from .forms import ContactForm


# Contact Form- Code adapted from (Django-2.2 Part-7 Django Contact Form with SMTP Email Backed Tutorial | By Creative web) 

def contact(request):
    Contact_Form = ContactForm
    if request.method == 'POST':
        form = Contact_Form(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name')
            contact_email = request.POST.get('contact_email')
            contact_content = request.POST.get('content')

            template = get_template('contact/contact_form.txt')
            context = {
                'contact_name' : contact_name,
                'contact_email' : contact_email,
                'contact_content' : contact_content,
            }
            
            content = template.render(context)

            email = EmailMessage(
                "New contact form email",
                content,
                "Pranita's T-shirt Shop" + '',
                ['pranitacoder12@gmail.com'],
                headers = { 'Reply To': contact_email }
            )

            email.send()
            messages.success(request, "You email has been successfully sent!") 
        if form.is_valid():
            return render (request, 'index')
        else:
            messages.error(request, "Error")      

    return render(request, 'contact/contact.html', {'contact_form':Contact_Form })

