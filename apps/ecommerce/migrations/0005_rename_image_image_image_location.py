# Generated by Django 3.2.9 on 2021-11-23 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("ecommerce", "0004_alter_image_product")]

    operations = [migrations.RenameField(model_name="image", old_name="image", new_name="image_location")]