# Generated by Django 4.0.3 on 2022-05-19 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("ecommerce", "0003_alter_category_slug_alter_category_title_and_more")]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        )
    ]