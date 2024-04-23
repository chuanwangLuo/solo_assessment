# Generated by Django 4.1.2 on 2024-04-15 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nutrition',
            old_name='alanine',
            new_name='cholesterol_mg',
        ),
        migrations.RenameField(
            model_name='nutrition',
            old_name='alcohol',
            new_name='choline_mg',
        ),
        migrations.RenameField(
            model_name='nutrition',
            old_name='arginine',
            new_name='folate_mcg',
        ),
        migrations.RenameField(
            model_name='nutrition',
            old_name='ash',
            new_name='folic_acid_mcg',
        ),
        migrations.RenameField(
            model_name='nutrition',
            old_name='aspartic_acid',
            new_name='niacin_mg',
        ),
        migrations.RenameField(
            model_name='nutrition',
            old_name='caffeine',
            new_name='pantothenic_acid_mg',
        ),
        migrations.RenameField(
            model_name='nutrition',
            old_name='calcium',
            new_name='saturated_fat_g',
        ),
        migrations.RenameField(
            model_name='nutrition',
            old_name='carbohydrate',
            new_name='sodium_mg',
        ),
        migrations.RenameField(
            model_name='nutrition',
            old_name='carotene_alpha',
            new_name='total_fat_g',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='carotene_beta',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='cholesterol',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='choline',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='copper',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='cryptoxanthin_beta',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='cystine',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='fat',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='fatty_acids_total_trans',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='fiber',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='folate',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='folic_acid',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='fructose',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='galactose',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='glucose',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='glutamic_acid',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='glycine',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='histidine',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='hydroxyproline',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='irom',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='isoleucine',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='lactose',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='leucine',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='lucopene',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='lutein_zeaxanthin',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='lysine',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='magnesium',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='maltose',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='manganese',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='methionine',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='monounsaturated_fatty_acids',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='niacin',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='pantothenic_acid',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='phenylalanine',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='phosphorous',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='polyunsaturated_fatty_acids',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='potassium',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='proline',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='protein',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='riboflavin',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='saturated_fat',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='saturated_fatty_acids',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='selenium',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='serine',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='sodium',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='sucrose',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='sugars',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='theobromine',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='thiamin',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='threonine',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='tocopherol_alpha',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='total_fat',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='tryptophan',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='tyrosine',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='valine',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='vitamin_a',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='vitamin_a_rae',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='vitamin_b12',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='vitamin_b6',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='vitamin_c',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='vitamin_d',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='vitamin_e',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='vitamin_k',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='water',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='zink',
        ),
    ]
