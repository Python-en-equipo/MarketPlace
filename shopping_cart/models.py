from django.db import models

from ecommerce.models import Product

# Create your models here.


class CartSession(models.Model):
    session_id = models.CharField(max_length=255, blank=True)
    data_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.session_id


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    cart = models.ForeignKey(CartSession, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_subtotal(self):
        return self.product.price * self.quantity

    def __unicode__(self):
        return self.product
