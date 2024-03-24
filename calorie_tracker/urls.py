from django.urls import path
from . import views
from .views import food_item_list, add_food_item, delete_food_item, suggest_recipe, calorie_intake

urlpatterns = [
    path('', views.food_item_list, name='food_item_list'),
    path('add/', views.add_food_item, name='add_food_item'),
    path('delete/<int:pk>/', views.delete_food_item, name='delete_food_item'),
    path('suggest_recipe/', suggest_recipe, name='suggest_recipe'),
    path('calorie_intake/', calorie_intake, name='calorie_intake'),
]
