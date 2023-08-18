from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=200)
    image = models.ImageField(upload_to='categories', blank=True, null=True)
    icon = models.CharField(max_length=50)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    amount = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products', blank=True, null=True)
    shop_id = models.ForeignKey('shops.Shop', on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"


class Review(models.Model):
    review = models.TextField(blank=True, null=True)
    stars = models.PositiveSmallIntegerField()
    date = models.DateField(auto_now_add=True, blank=True)
    shop_id = models.ForeignKey('shops.Shop', on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_id = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)

    def __str__(self):
        return self.review

    class Meta:
        verbose_name = "review"
        verbose_name_plural = "reviews"
        ordering = ["-date"]
