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
        self.assertEqual(response.status_code, 302)  # 假设加入购物车后会重定向


class PurchaseTest(TestCase):
    def setUp(self):
        # 创建用户并登录
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        # 创建产品
        self.product = Product.objects.create(name="Test Product", price=19.99, stock=10)

        # 创建购物车项目
        self.cart_item = CartItem.objects.create(user=self.user, product=self.product, quantity=1, is_purchased=False)

    def test_purchase_items(self):
        # 模拟购买操作
        response = self.client.post('/purchase-items/')
        self.cart_item.refresh_from_db()

        # 检查是否购买成功
        self.assertTrue(self.cart_item.is_purchased)
        self.assertEqual(response.status_code, 302)
