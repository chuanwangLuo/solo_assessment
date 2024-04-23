from django.test import TestCase
from myapp.models import Product

class ProductModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name="ANDREA'S, Gluten Free Soft Dinner Roll", price=14.36, stock=100)

    def test_string_representation(self):
        self.assertEqual(str(self.product), "ANDREA'S, Gluten Free Soft Dinner Roll")

    def test_stock_update(self):
        self.product.stock = 100
        self.product.save()
        self.assertEqual(Product.objects.get(id=self.product.id).stock, 100)
