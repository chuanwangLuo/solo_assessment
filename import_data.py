import os
import django
import pandas as pd


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')


django.setup()

from myapp.models import Nutrition 

def import_excel_data():
    data = pd.read_excel('data/nutrition.xlsx')  

    for _, row in data.iterrows():
        row = row.where(pd.notna(row), None)

        
        Nutrition.objects.create(
            name=row['name'],
            serving_size=row['serving_size'],
            calories=row['calories'],
            total_fat_g=row['total_fat_g'],
            saturated_fat_g=row['saturated_fat_g'],	
            cholesterol_mg=row['cholesterol_mg'],
            sodium_mg=row['sodium_mg'],
            choline_mg=row['choline_mg'],
            folate_mcg=row['folate_mcg'],
            folic_acid_mcg=row['folic_acid_mcg'],
            niac_mg=row['niac_mg'],
            pantothenic_acid_mg=row['pantothenic_acid_mg'],	

        )
        print(f"Imported {row['name']}")


if __name__ == '__main__':
    import_excel_data()
