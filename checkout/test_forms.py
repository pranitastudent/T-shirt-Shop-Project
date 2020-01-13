from django.test import TestCase
from checkout.forms import MakePaymentForm, OrderForm

# Code Adapated from Django Testing Tutorial - Testing Forms #5 - The DumbFounds
class TestOrderForm(TestCase):

    # First test - insertion of personal details

    def test_can_make_payment_with_required_values(self):
        form = OrderForm({
            'full_name': "test",
            'phone_number': "test",
            'country': "test",
            'postcode': "test",
            'town_or_city': "test",
            'street_address1': "test",
            'street_address2': "test",
            'county': "test"
        })
        self.assertTrue(form.is_valid())

    # Second Test - insertion of creditcard numbers and stripe id

    # Payment can be made


class TestPaymentMethod(TestCase):

    def test_can_payment_be_made_required_values(self):

        form = MakePaymentForm({
            'credit_card_number': '4242424242424242',
            'cvv': 222,
            'expiry_month': 5,
            'expiry_year': 2021,
            'stripe_id': 'test'
        })

        self.assertTrue(form.is_valid())

# Payment can't be made - with no stripe id


class TestPaymentMethod(TestCase):
    def test_cannot_payment_be_made_required_values(self):

        form = MakePaymentForm({
            'credit_card_number': '4242424242424242',
            'cvv': 222,
            'expiry_month': 5,
            'expiry_year': 2021,

        })
        self.assertFalse(form.is_valid())
