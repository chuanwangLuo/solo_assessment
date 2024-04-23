from django.test import TestCase
from myapp.models import Product
from django.urls import reverse
from django.core.exceptions import ValidationError

class ProductExistenceTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Product.objects.create(name="Cornstarch", price=6.46)

    def test_product_existence(self):
        """检查特定商品是否存在"""
        exists = Product.objects.filter(name="Cornstarch").exists()
        self.assertTrue(exists)



class AccessControlTest(TestCase):
    def test_cart_access_for_unauthenticated_user(self):
        """测试未认证用户访问购物车是否被重定向到登录页面"""
        response = self.client.get(reverse('cart'))
        self.assertRedirects(response, f"{reverse('login')}?next={reverse('cart')}")




class ProductDataIntegrityTest(TestCase):
    def test_product_creation_without_price(self):
        """尝试创建没有价格的商品应该抛出错误"""
        with self.assertRaises(ValidationError):
            Product.objects.create(name="Incomplete Product").full_clean()
