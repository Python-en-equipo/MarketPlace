from django.core.validators import MinValueValidator
from django.db import models
from django.template.defaultfilters import slugify

from users.models import Seller


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, null=True, blank=True, unique=True)

    class Meta:

        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)


class Product(models.Model):
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE, null=True, blank=True)
    seller = models.ForeignKey(
        Seller, related_name="products", on_delete=models.CASCADE, null=True, blank=True
    )  # momentaneo, hay que modificar tests!!
    title = models.CharField(max_length=250)
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

        # LOGICA PARA LAS URLS UNICAS
        original_slug = slugify(self.title)  # creacion automatica apartir del titulo
        queryset = Product.objects.all().filter(slug__iexact=original_slug).count()
        # "Busca si hay otro slug que conincida con el mismo original_slug"
        count = 1
        slug = original_slug
        # (queryset) si encuentra otro con este mismo slug
        while queryset:
            slug = original_slug + "-" + str(count)
            count += 1
            # vuelve a hacer la verificacion
            queryset = Product.objects.all().filter(slug__iexact=slug).count()
        self.slug = slug



class Image(models.Model):
    product = models.ForeignKey(Product, related_name="product_images", on_delete=models.CASCADE)
    image_location = models.ImageField(upload_to="media/products/", null=True, blank=True)
