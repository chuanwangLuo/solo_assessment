import random
from django.core.management.base import BaseCommand
from myapp.models import Product
from django.db import transaction

class Command(BaseCommand):
    help = 'Updates products with a default price'

    def handle(self, *args, **options):
        try:
            with transaction.atomic():
                products = Product.objects.filter(price=0)
                for product in products:
                    product.price = random.uniform(5.99, 19.99)
                    product.save()
                self.stdout.write(self.style.SUCCESS(f'Successfully updated {len(products)} products.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error updating products: {str(e)}'))