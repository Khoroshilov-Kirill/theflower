from django.shortcuts import render
from .models import Shop
from django.shortcuts import redirect


def shops(request, slug):
    shops = Shop.objects.filter(slug=slug)
    return render(request, "shops/shops.html", {'shops': shops})


def index(request):
    shops = Shop.objects.all().values('city','slug').distinct()
    return render(request, "shops/index.html", {'shops': shops})


def red(request, slug, pk):
    return redirect('product', shop_id=pk)

