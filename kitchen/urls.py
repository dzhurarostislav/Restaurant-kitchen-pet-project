from django.contrib import admin
from django.urls import path, include

from kitchen.views import (
    index,
    CookCreateView,
    CookListView,
    CookDetailView,
    CookUpdateView,
    IngredientListView,
    IngredientCreateView,
    IngredientUpdateView,
    DishListView,
    DishCreateView,
    DishDetailView,
    DishUpdateView,
)

urlpatterns = [
    path("", index, name="home"),
    path("register/", CookCreateView.as_view(), name="create-cook"),
    path("cooks/", CookListView.as_view(), name="cooks-list"),
    path("cooks/<int:pk>", CookDetailView.as_view(), name="cook-detail"),
    path(
        "cooks/<int:pk>/update",
        CookUpdateView.as_view(),
        name="cook-update"
    ),
    path(
        "ingredients/",
        IngredientListView.as_view(),
        name="ingredient-list"
    ),
    path(
        "ingredients/create/",
        IngredientCreateView.as_view(),
        name="ingredient-create"
    ),
    path(
        "ingredients/<int:pk>/update/",
        IngredientUpdateView.as_view(),
        name="ingredient-update"
    ),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path(
        "dishes/<int:pk>/update",
        DishUpdateView.as_view(),
        name="dish-update"
    ),
]

app_name = "kitchen"
