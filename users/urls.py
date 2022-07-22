from django.urls import path
from . import views

app_name = "users"


urlpatterns = [
    path("register/", views.register, name="register"),
    path("login", views.loginusers, name="login"),
    path("logout", views.logoutusers, name="logout"),
]