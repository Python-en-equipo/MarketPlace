# Generated by Django 4.0.3 on 2022-05-18 01:13

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=255, unique=True)),
                ("slug", models.SlugField(max_length=255)),
            ],
            options={"verbose_name": "category", "verbose_name_plural": "categories"},
        ),
        migrations.CreateModel(
            name="Image",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("image_location", models.ImageField(blank=True, null=True, upload_to="media/products/")),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=250)),
                ("description", models.TextField()),
                ("price", models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(50)])),
                ("slug", models.SlugField(blank=True, null=True)),
                ("stock", models.PositiveIntegerField(default=0)),
                ("is_available", models.BooleanField(default=False)),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="ecommerce.category",
                    ),
                ),
            ],
        ),
    ]
