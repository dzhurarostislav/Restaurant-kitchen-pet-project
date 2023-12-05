from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from kitchen.forms import CookCreationForm, CookUpdateForm
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


class CookCreateView(generic.CreateView):
    model = Cook
    form_class = CookCreationForm
    template_name = "kitchen/register.html"
    success_url = reverse_lazy("kitchen:home")

    def form_valid(self, form) -> HttpResponse:
        response = super().form_valid(form)
        login(self.request, self.object)

        return response


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    context_object_name = "cook_list"
    template_name = "kitchen/cooks-list.html"
    paginate_by = 5


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook
    context_object_name = "cook_detail"
    template_name = "kitchen/cook-detail.html"


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    form_class = CookUpdateForm
    template_name = "kitchen/cook-update.html"
    success_url = reverse_lazy("kitchen:cooks-list")
