from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):

    STATUS = (
        ('customer', 'customer'),
        ('owner', 'owner'),
        ('cashier', 'cashier'),
    )

    email = models.EmailField(unique=True)
    status = models.CharField(max_length=64, choices=STATUS, default='customer')
    phone = models.CharField(max_length=20, null=True)
    image = models.ImageField(upload_to='users', blank=True, null=True)

    def __str__(self):
        return self.username
