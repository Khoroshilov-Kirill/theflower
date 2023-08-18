from django.urls import path

from . import views

urlpatterns = [
    path("<int:shop_id>", views.product, name="product"),
    path("<int:category_id>/<int:shop_id>/", views.prodcategory, name="prodcategory"),
    path("details/<int:pk>/<int:shop_id>/", views.details, name="details"),
]