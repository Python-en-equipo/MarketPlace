from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse

class Product(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    price = models.PositiveIntegerField(validators=[MinValueValidator(50)])

    def __str__(self):
        return self.title

    def was_created(self):
        if  self.price < 50:
            return False
        return True

    # def get_absolute_url(self):
    #     return reverse("detail", kwargs={"id": self.id})