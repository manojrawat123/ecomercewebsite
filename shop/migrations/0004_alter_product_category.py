# Generated by Django 4.1.5 on 2023-03-30 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('M', 'mobile'), ('L', 'Laptop'), ('TW', 'Top Wear'), ('SH', 'Bottom Wear'), ('TS', 'tShirt'), ('SHOES', 'Shoes'), ('EV', 'eletronic Vechile'), ('PV', 'Vechile'), ('BK', 'Bike')], max_length=3000),
        ),
    ]
