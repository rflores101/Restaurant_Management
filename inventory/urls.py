from django.urls import include, path

from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("logout/", views.logout_view, name="logout"),
    path('accounts/login/', auth_views.LoginView.as_view(), name="login"),
    path('', views.home, name='home'),
    path('ingredients/', views.IngredientList.as_view(), name='ingredients'),
    path('ingredients/<pk>/delete', views.IngredientDelete.as_view(), name='ingredientdelete'),
    path('ingredients/create', views.IngredientCreate.as_view(), name='ingredientcreate'),
    path('ingredients/<pk>/update/', views.IngredientUpdate.as_view(), name='ingredientupdate'),
    path('menu/', views.MenuItemList.as_view(), name='menu'),
    path('menu/<pk>/recipe/', views.RecipeRequirementList.as_view(), name='recipe'),
    path('recipe/create/', views.RecipeRequirementCreate.as_view(), name='reciperequirementcreate'),
    path('recipe/<pk>/update/', views.RecipeRequirementUpdate.as_view(), name='reciperequirementupdate'),
    path('recipe/<pk>/delete/', views.RecipeRequirementDelete.as_view(), name='reciperequirementdelete'),
    path('menu/create/', views.MenuItemCreate.as_view(), name='menuitemcreate'),
    path('purchases/', views.PurchaseList.as_view(), name='purchases'),
    path('purchases/create/', views.PurchaseCreate.as_view(), name='purchasecreate'),
    path('purchases/<pk>/delete/', views.PurchaseDelete.as_view(), name='purchasedelete'),
    path('finances/', views.FinanceView.as_view(), name='finances'),
]