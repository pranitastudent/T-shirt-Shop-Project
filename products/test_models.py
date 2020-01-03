from django.test import TestCase
from products.models import Product

class ProductTest(TestCase):
    
    def test_product_category_str_test(self):
        test_product = Product(product_name="product",
                               price=4.99,
                               category="test",
                               product_date= "2020-05-06")
        self.assertEqual(str(test_product.category), "test")
        
