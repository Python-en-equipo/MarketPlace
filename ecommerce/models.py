from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    price = models.IntegerField()