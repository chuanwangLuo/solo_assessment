import random
from django.core.management.base import BaseCommand
from myapp.models import Nutrition, Product

class Command(BaseCommand):
    help = 'Imports data from Nutrition model to Product model'

    def handle(self, *args, **options):
        batch_size = 100  # Process 100 objects at a time
        total_count = Nutrition.objects.count()
        for start in range(0, total_count, batch_size):
            end = start + batch_size
            nutrition_objects = Nutrition.objects.all()[start:end]
            for nutrition in nutrition_objects:
                self.update_product(nutrition)

    def update_product(self, nutrition):
        description = self.build_description(nutrition)
        price = random.uniform(5.99, 19.99)
        stock = 100
        product, created = Product.objects.get_or_create(name=nutrition.name)
        product.description = description
        product.price = price
        product.stock = stock
        product.save()
        self.stdout.write(self.style.SUCCESS(f'Updated product for {nutrition.name}'))

    def build_description(self, nutrition):
        return (
            f"Calories (kj): {nutrition.calories}, "
            f"Total fat (g): {nutrition.total_fat_g}, "
            f"Saturated fat (g): {nutrition.saturated_fat_g}, "
            f"Cholesterol (mg): {nutrition.cholesterol_mg}, "
            f"Sodium (mg): {nutrition.sodium_mg}, "
            f"Choline (mg): {nutrition.choline_mg}, "
            f"Folate (mcg): {nutrition.folate_mcg}, "
            f"Folic acid (mcg): {nutrition.folic_acid_mcg}, "
            f"Niac (mg): {nutrition.niac_mg}, "
            f"Pantothenic acid (mg): {nutrition.pantothenic_acid_mg}"
        )
