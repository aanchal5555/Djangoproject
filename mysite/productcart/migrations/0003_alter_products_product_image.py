# Generated by Django 4.1.4 on 2023-08-30 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productcart', '0002_alter_products_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_image',
            field=models.ImageField(default=None, max_length=250, null=True, upload_to='products/'),
        ),
    ]
