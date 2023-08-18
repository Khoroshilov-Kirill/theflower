from django.contrib import admin
from .models import Shop


class MemberShop(admin.ModelAdmin):
    list_display = ('name', 'city', 'slug')
    prepopulated_fields = {"slug": ('city',)}


admin.site.register(Shop, MemberShop)