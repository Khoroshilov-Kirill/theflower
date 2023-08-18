from django.contrib import admin

from .models import Category, Product, Review


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'amount', 'price', 'shop_id')
    search_fields = ('title', )


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user_id','shop_id', 'product_id', 'review')


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
