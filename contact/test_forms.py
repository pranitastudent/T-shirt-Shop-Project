from django.test import TestCase
from contact.forms import ContactForm

class TestContactForm(TestCase):
    
    def contact_form_required_values(self):
        form = ContactForm({
            "contact_name":"test",
            "contact_email":"test",
            "content":"test"
            
        })
        self.assertTrue(form.is_valid())
        