from django.core.validators import MinValueValidator
from django.db import models
from django.template.defaultfilters import slugify

from users.models import Seller


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, default=slugify(title))

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)


class Product(models.Model):
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE, default=1)
    seller = models.ForeignKey(
        Seller, related_name="products", on_delete=models.CASCADE, null=True, blank=True
    )  # momentaneo, hay que modificar tests!!
    title = models.CharField(max_length=250, unique=True)
    description = models.TextField()
    price = models.PositiveIntegerField(validators=[MinValueValidator(50)])
    slug = models.SlugField(null=True, blank=True, unique=True)
    stock = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def was_created(self):
        if self.price < 50:
            return False
        return True

    def save(self, *args, **kwargs):
        self.is_available = False
        self.slug = slugify(self.title)
        if self.stock > 0:
            self.is_available = True
        super(Product, self).save(*args, **kwargs)


class Image(models.Model):
    product = models.ForeignKey(Product, related_name="product_images", on_delete=models.CASCADE)
    image_location = models.ImageField(upload_to="products/", null=True, blank=True)
