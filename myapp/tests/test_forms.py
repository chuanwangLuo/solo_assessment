from django.test import TestCase
from myapp.models import Product
from django.urls import reverse
from django.core.exceptions import ValidationError

class ProductExistenceTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Product.objects.create(name="Cornstarch", price=6.46)

    def test_product_existence(self):
        """ Check for the presence of a particular commodity """
        exists = Product.objects.filter(name="Cornstarch").exists()
        self.assertTrue(exists)



class AccessControlTest(TestCase):
    def test_cart_access_for_unauthenticated_user(self):
        """ Tests if unauthenticated users accessing the cart is redirected to the login page """
        response = self.client.get(reverse('cart'))
        self.assertRedirects(response, f"{reverse('login')}?next={reverse('cart')}")




class ProductDataIntegrityTest(TestCase):
    def test_product_creation_without_price(self):
        """ Trying to create an item without a price should throw an error """
        with self.assertRaises(ValidationError):
            Product.objects.create(name="Incomplete Product").full_clean()
