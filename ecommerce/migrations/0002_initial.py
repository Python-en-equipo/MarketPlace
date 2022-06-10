# Generated by Django 4.0.3 on 2022-05-18 01:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [("ecommerce", "0001_initial"), ("users", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="product",
            name="seller",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="products",
                to="users.seller",
            ),
        ),
        migrations.AddField(
            model_name="image",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="product_images", to="ecommerce.product"
            ),
        ),
    ]
