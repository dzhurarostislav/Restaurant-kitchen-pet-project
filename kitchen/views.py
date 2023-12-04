from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from kitchen.models import Dish, Cook, Ingredient

@login_required
def index(request: HttpRequest) -> HttpResponse:
    """View function for the home page of the site."""

    num_dishes = Dish.objects.count()
    num_cooks = Cook.objects.count()
    num_ingredients = Ingredient.objects.count()
    context = {
        "num_dishes": num_dishes,
        "num_cooks": num_cooks,
        "num_ingredients": num_ingredients,
    }

    return render(request, "kitchen/index.html", context=context)
