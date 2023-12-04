from django.contrib import admin
from django.urls import path, include

from kitchen.views import index

urlpatterns = [
    path("", index, name="home"),
]

app_name = "kitchen"
