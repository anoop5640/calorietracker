from django.shortcuts import render
import requests
# Create your views here.
from django.shortcuts import render, redirect
from .models import FoodItem
from .forms import FoodItemForm
from django.db.models import Sum

def food_item_list(request):
    items = FoodItem.objects.all()
    total_calories = items.aggregate(total=Sum('calories'))['total'] or 0
    return render(request, 'calorie_tracker/food_item_list.html', {'items': items, 'total_calories': total_calories})

def add_food_item(request):
    if request.method == "POST":
        form = FoodItemForm(request.POST)
        if form.is_valid():
            # Extract the food name from the form
            food_name = form.cleaned_data['name']

            # Make an API request to get calorie information
            response = requests.get(f"http://127.0.0.1:8080/api/calories?food_name={food_name}")
            if response.status_code == 200:
                calorie_data = response.json()
                calories = calorie_data.get('calories', 0) # Assuming the API returns a JSON with a 'calories' field

                # Save the FoodItem with the calorie data from the API
                FoodItem.objects.create(name=food_name, calories=calories)
                return redirect('food_item_list')
            else:
                # Handle cases where the API call fails
                print("Failed to fetch calorie information. Status Code:", response.status_code)
                # You might want to redirect to an error page or display an error message
    else:
        form = FoodItemForm()
    return render(request, 'calorie_tracker/add_food_item.html', {'form': form})

def delete_food_item(request, pk):
    FoodItem.objects.filter(id=pk).delete()
    return redirect('food_item_list')
