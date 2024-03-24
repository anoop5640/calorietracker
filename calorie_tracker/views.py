from django.shortcuts import render
import requests
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import FoodItem
from .forms import FoodItemForm, IngredientForm, CalorieIntakeForm
from django.db.models import Sum

def food_item_list(request):
    items = FoodItem.objects.all()
    total_calories = items.aggregate(total=Sum('calories'))['total'] or 0
    return render(request, 'calorie_tracker/food_item_list.html', {'items': items, 'total_calories': total_calories})

def add_food_item(request):
    form = FoodItemForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        food_name = form.cleaned_data['name']

        # Make an API request to get calorie information
        response = requests.get(f"http://127.0.0.1:8080/api/calories?food_name={food_name}")
        if response.status_code == 200:
            calorie_data = response.json()
            calories = calorie_data.get('calories')

            # Check if the calories data is an integer
            if isinstance(calories, int):
                FoodItem.objects.create(name=food_name, calories=calories)
                messages.success(request, f"Food item '{food_name}' added with {calories} calories.")
                return redirect('food_item_list')
            else:
                # If the API doesn't return an integer for calories, inform the user
                messages.error(request, "Calorie information for this food item was not found.")
        else:
            # Handle cases where the API call fails
            messages.error(request, f"Failed to fetch calorie information. Status Code: {response.status_code}")
    
    # If it's a GET request or the form is not valid, render the page with the form
    return render(request, 'calorie_tracker/add_food_item.html', {'form': form})

def delete_food_item(request, pk):
    FoodItem.objects.filter(id=pk).delete()
    return redirect('food_item_list')

def suggest_recipe(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            ingredients = form.cleaned_data['ingredients']
            api_url = f"http://127.0.0.1:8000/api/recipes/suggest/?ingredients={ingredients}"
            response = requests.get(api_url)
            if response.status_code == 200:
                recipes = response.json()  # Assuming the API returns a list of recipes
                return render(request, 'calorie_tracker/suggest_recipe.html', {'form': form, 'recipes': recipes})
            else:
                # Handle API errors
                recipes = []
    else:
        form = IngredientForm()
        recipes = []
    return render(request, 'calorie_tracker/suggest_recipe.html', {'form': form, 'recipes': recipes})

def calorie_intake(request):
    if request.method == 'POST':
        form = CalorieIntakeForm(request.POST)
        if form.is_valid():
            height = form.cleaned_data['height']
            weight = form.cleaned_data['weight']
            response = requests.get(
                "http://calorieapi-env.eba-udbdxf3g.us-east-1.elasticbeanstalk.com/api/calorie_intake",
                params={'height': height, 'weight': weight}
            )
            if response.status_code == 200:
                recommended_intake = response.json().get('calorie_intake')
                # You can now pass this data to your template or further process it.
            else:
                # Handle errors
                pass  # Remember to replace 'pass' with actual error handling
    else:
        form = CalorieIntakeForm()
        recommended_intake = None  # Make sure this variable is defined outside the POST check if it's used in the template

    # Render your form with context here
    return render(request, 'calorie_tracker/calorie_intake.html', {'form': form, 'recommended_intake': recommended_intake})