# Generated by Django 4.0.1 on 2022-01-25 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0007_alter_image_image_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_location',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
    ]
