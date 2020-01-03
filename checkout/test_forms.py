from django.test import TestCase
from checkout.forms import MakePaymentForm, OrderForm

class TestOrderForm(TestCase):
    
    def test_can_make_payment_with_required_values(self):
        form = OrderForm({
            'full_name':"test",
            'phone_number':"test",
            'country': "test",
            'postcode': "test",
            'town_or_city':"test",
            'street_address1':"test",
            'street_address2':"test",
        })
        self.assertTrue(form.is_valid())
     