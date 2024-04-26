from django.db import models
from django.conf import settings


class Nutrition(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    serving_size = models.CharField(max_length=100, blank=True, null=True)
    calories = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_fat_g = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    saturated_fat_g = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cholesterol_mg = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sodium_mg = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    choline_mg = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    folate_mcg = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    folic_acid_mcg = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    niac_mg = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pantothenic_acid_mg = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Nutrition Data"


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    nutrition = models.OneToOneField(Nutrition, on_delete=models.SET_NULL, null=True, related_name='product')

    def __str__(self):
        return self.name


class CartItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    is_purchased = models.BooleanField(default=False)  # Add purchase status field

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
