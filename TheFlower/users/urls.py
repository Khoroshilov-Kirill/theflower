from django.urls import path

from . import views

urlpatterns = [
    path("register", views.registration, name="register"),
    path("logout", views.logout_view, name="logout"),
    path("login", views.login_view, name="login"),
    path("profile/<int:pk>", views.Profile.as_view(), name="profile"),
]