from django.db import models
from ecommerce.models import Product
from users.models import CustomUser

# Create your models here.


class CartItem(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user_id = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    total = models.DecimalField(max_digits=10,decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


class OrderDetails(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.PROTECT)
    order_id = models.ForeignKey(OrderItem, on_delete=models.PROTECT)
    preci = models.DecimalField(max_digits=10,decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


class PaymentDetails(models.Model):
    pass
