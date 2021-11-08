from django.db import models
from django.urls import reverse

class Product(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    price = models.IntegerField()

    # def get_absolute_url(self):
    #     return reverse("detail", kwargs={"id": self.id})