from django.contrib import admin
from django.urls import path, include

from kitchen.views import index, CookCreateView

urlpatterns = [
    path("", index, name="home"),
    path("register/", CookCreateView.as_view(), name="create-cook"),

]

app_name = "kitchen"
