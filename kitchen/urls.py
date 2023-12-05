from django.contrib import admin
from django.urls import path, include

from kitchen.views import index, CookCreateView, CookListView, CookDetailView, CookUpdateView

urlpatterns = [
    path("", index, name="home"),
    path("register/", CookCreateView.as_view(), name="create-cook"),
    path("cooks/", CookListView.as_view(), name="cooks-list"),
    path("cooks/<int:pk>", CookDetailView.as_view(), name="cook-detail"),
    path("cooks/<int:pk>/update", CookUpdateView.as_view(), name="cook-update"),
]

app_name = "kitchen"
