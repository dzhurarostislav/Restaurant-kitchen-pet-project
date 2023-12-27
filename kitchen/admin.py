from django.contrib import admin
from .models import DishType, IngredientType, Ingredient, Cook, Dish


@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(IngredientType)
class IngredientTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'type')


@admin.register(Cook)
class CookAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'years_of_experience')


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'dish_type')
