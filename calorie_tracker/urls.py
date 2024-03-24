from django.urls import path
from . import views

urlpatterns = [
    path('', views.food_item_list, name='food_item_list'),
    path('add/', views.add_food_item, name='add_food_item'),
    path('delete/<int:pk>/', views.delete_food_item, name='delete_food_item'),
]
