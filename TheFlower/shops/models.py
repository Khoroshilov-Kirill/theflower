from django.db import models
from .serializer import social_default_value


class Shop(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    social = models.JSONField(default=social_default_value)
    image = models.ImageField(upload_to='shops', blank=True, null=True)
    slug = models.SlugField(default='', null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "shop"
        verbose_name_plural = "shops"
        ordering = ('city',)
