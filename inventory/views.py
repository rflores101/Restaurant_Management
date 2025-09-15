from typing import Any
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import IngredientCreateForm, IngredientUpdateForm, MenuItemCreateForm, RecipeRequirementCreateForm, PurchaseCreateForm, RecipeRequirementUpdateForm
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
    return render(request, "inventory/home.html")

def logout_view(request):
    logout(request)
    return redirect("/")

class IngredientList(LoginRequiredMixin, ListView):
    model = Ingredient
    template_name = "inventory/ingredients.html"
    context_object_name = "ingredients"

class IngredientCreate(LoginRequiredMixin, CreateView):
    model = Ingredient
    form_class = IngredientCreateForm
    template_name = "inventory/ingredient_create_form.html"
    success_url = "/ingredients"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        if form.is_valid():
            form.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

class IngredientUpdate(LoginRequiredMixin, UpdateView):
    model = Ingredient
    form_class = IngredientUpdateForm
    template_name = "inventory/ingredient_update_form.html"
    success_url = "/ingredients"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        if form.is_valid():
            form.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

class IngredientDelete(LoginRequiredMixin, DeleteView):
    model = Ingredient
    template_name = "inventory/ingredient_delete_view.html"
    success_url = "/ingredients"



class MenuItemList(LoginRequiredMixin, ListView):
    model = MenuItem
    template_name = "inventory/menu.html"
    context_object_name = "menu_items"

class MenuItemCreate(LoginRequiredMixin, CreateView):
    model = MenuItem
    form_class = MenuItemCreateForm
    template_name = "inventory/menu_item_create_form.html"
    success_url = "/menu"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        if form.is_valid():
            form.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)



class RecipeRequirementList(LoginRequiredMixin, ListView):
    model = RecipeRequirement
    template_name = "inventory/recipe_requirement.html"
    context_object_name = "requirements"

class RecipeRequirementCreate(LoginRequiredMixin, CreateView):
    model = RecipeRequirement
    form_class = RecipeRequirementCreateForm
    template_name = "inventory/recipe_requirement_create_form.html"
    success_url = "/menu/<pk>/recipe"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        if form.is_valid():
            form.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

class RecipeRequirementUpdate(LoginRequiredMixin, UpdateView):
    model = RecipeRequirement
    form_class = RecipeRequirementUpdateForm
    template_name = "inventory/recipe_requirement_update_form.html"
    success_url = "/menu/<pk>/recipe"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        if form.is_valid():
            form.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

class RecipeRequirementDelete(LoginRequiredMixin, DeleteView):
    model = RecipeRequirement
    template_name = "inventory/recipe_requirement_delete_view.html"
    success_url = "/menu/<pk>/recipe"



class PurchaseList(LoginRequiredMixin, ListView):
    model = Purchase
    template_name = "inventory/purchases.html"
    context_object_name = "purchases"

class PurchaseCreate(LoginRequiredMixin, CreateView):
    model = Purchase
    form_class = PurchaseCreateForm
    template_name = "inventory/purchase_create_form.html"
    success_url = "/purchases"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        if form.is_valid():
            form.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

class PurchaseDelete(LoginRequiredMixin, DeleteView):
    model = Purchase
    template_name = "inventory/purchase_delete_view.html"
    success_url = "/purchases"



class FinanceView(LoginRequiredMixin, TemplateView):
    template_name = "inventory/finances.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        ingredients = Ingredient.objects.all()
        purchases = Purchase.objects.all()
        revenue = 0
        expenses = 0
        for i in range(len(purchases)):
            revenue += purchases[i].menu_item.price

        for i in range(len(ingredients)):
            expenses += round((ingredients[i].quantity * ingredients[i].unit_price),2)

        profit = revenue - expenses

        context['revenue'] = revenue
        context['expenses'] = expenses
        context['profit'] = profit

        return context
    

        








        

        


