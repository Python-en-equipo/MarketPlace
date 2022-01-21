# Generated by Django 3.2.9 on 2021-11-23 09:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("ecommerce", "0003_image")]

    operations = [
        migrations.AlterField(
            model_name="image",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="product_images", to="ecommerce.product"
            ),
        )
    ]
