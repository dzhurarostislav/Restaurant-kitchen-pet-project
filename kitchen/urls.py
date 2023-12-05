from django.contrib import admin
from django.urls import path, include

from kitchen.views import index, CookCreateView, CookListView

urlpatterns = [
    path("", index, name="home"),
    path("register/", CookCreateView.as_view(), name="create-cook"),
    path("cooks/", CookListView.as_view(), name="cooks-list"),
]

app_name = "kitchen"
