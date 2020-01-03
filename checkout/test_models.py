from django.test import TestCase
from checkout.models import Order

class OrderTests(TestCase):
    
    def test_country_str_test(self):
        test_order = Order(full_name="test",
                           phone_number = "test",
                           country="france",
                           postcode="test",
                           town_or_city="test",
                           street_address1="test",
                           street_address2="test",
                           county="test",
                           date="2020-01-01")
        self.assertEqual(str(test_order.country), "france")                   
                       
