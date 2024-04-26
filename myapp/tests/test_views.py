from django.urls import reverse
from django.test import TestCase
from myapp.models import Product,CartItem
from django.contrib.auth.models import User

class ProductListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        for i in range(5):
            Product.objects.create(name=f'Product {i}', price=10.00 + i)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 404)

class ProductDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.product = Product.objects.create(name='Cornstarch', price=6.46)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('product_detail', kwargs={'id': self.product.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'myapp/product_detail.html')

class CartTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.product = Product.objects.create(name="Test Product", price=19.99, stock=10)
        self.client.login(username='testuser', password='testpassword')

    def test_add_to_cart(self):
        response = self.client.post(f'/add-to-cart/{self.product.id}/')
        self.assertEqual(response.status_code, 302)  # Assume redirection after adding to cart


class PurchaseTest(TestCase):
    def setUp(self):
        # Create a user and log in
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        # Create Products
        self.product = Product.objects.create(name="Test Product", price=19.99, stock=10)

        # Create a shopping cart item
        self.cart_item = CartItem.objects.create(user=self.user, product=self.product, quantity=1, is_purchased=False)

    def test_purchase_items(self):
        # Simulate the purchase operation
        response = self.client.post('/purchase-items/')
        self.cart_item.refresh_from_db()

        # Check whether the purchase was successful
        self.assertTrue(self.cart_item.is_purchased)
        self.assertEqual(response.status_code, 302)
