from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

# administra al customuser


class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""
    def _create_user(self, email, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


# user general que se autenticará con email
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    """ Hay que agregar estos datos a todos los usuarios clientes y vendedores"""
    # user  = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="profile", primary_key=True)
    # first_name = models.CharField(max_length=20, null=True, blank=True)
    # last_name = models.CharField(max_length=40, null=True, blank=True)
    # address = models.CharField(max_length=170, null=True, blank=True)
    # joined_at = models.DateTimeField(auto_now_add=True)
    # #phone_number = PhoneNumberField(unique=True, blank=True) # no encuentro este modulo

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # necesita de un manager que lo administre para crearlo con ciertos campos
    objects = CustomUserManager()


class Seller(models.Model):
    profile = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="seller", primary_key=True)
    seller_name = models.CharField(max_length=50)
    #is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.seller_name}"
