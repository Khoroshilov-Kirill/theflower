from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("shops/<slug:slug>/", views.shops, name="shops"),
    path("shops/<slug:slug>/<int:pk>", views.red, name='redirect')

]