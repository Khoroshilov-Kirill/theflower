from django.shortcuts import render, redirect
from .models import Category, Product, Review
from .forms import SendReview
from shops.models import Shop
from django.db.models import Avg



def product(request,shop_id):
    cat = Category.objects.all()
    prod = Product.objects.filter(shop_id=shop_id)
    return render(request, "products/products.html", {'products': prod, 'categories': cat, 'shop_id': shop_id})


def prodcategory(request, category_id, shop_id):
    cat = Category.objects.all()
    prod = Product.objects.filter(category_id=category_id, shop_id=shop_id)
    return render(request, "products/products.html", {'products': prod, 'categories': cat, 'shop_id': shop_id})


def details(request, pk, shop_id):
    cat = Category.objects.all()
    prod = Product.objects.filter(pk=pk)
    reviews = Review.objects.filter(product_id=pk)
    shop = Shop.objects.get(pk=shop_id)
    avg_stars = reviews.aggregate(Avg('stars'))
    context = {'products': prod,'categories': cat, 'shop_id': shop_id, 'reviews': reviews, 'stars': avg_stars}
    if request.method == 'POST':
        form = SendReview(request.POST)
        if form.is_valid and request.user.is_authenticated:
            instance = form.save(commit=False)
            instance.user_id = request.user
            instance.stars = request.POST.get('ratings')
            instance.shop_id = shop
            instance.product_id = prod[0]
            instance.save()
            return redirect(request.META['HTTP_REFERER'])
        else:
            return redirect('login')

    form = SendReview()
    context['formReview'] = form
    return render(request, "products/products_details.html", context=context)
