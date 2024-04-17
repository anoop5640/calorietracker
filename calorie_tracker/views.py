from django.shortcuts import render
import requests
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import FoodItem
from .forms import FoodItemForm, IngredientForm, CalorieIntakeForm
from django.db.models import Sum
# Create your views here.
def food_item_list(request):
    items = FoodItem.objects.all()
    total_calories = items.aggregate(total=Sum('calories'))['total'] or 0
    return render(request, 'calorie_tracker/food_item_list.html', {'items': items, 'total_calories': total_calories})
#view for adding food item
def add_food_item(request):
    form = FoodItemForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        food_name = form.cleaned_data['name']

        
        response = requests.get(f"http://calorieapi-env.eba-kzssi36i.us-east-1.elasticbeanstalk.com/api/calories?food_name={food_name}")
        if response.status_code == 200:
            calorie_data = response.json()
            calories = calorie_data.get('calories')

            
            if isinstance(calories, int):
                FoodItem.objects.create(name=food_name, calories=calories)
                messages.success(request, f"Food item '{food_name}' added with {calories} calories.")
                return redirect('food_item_list')
            else:
                
                messages.error(request, "Calorie information for this food item was not found.")
        else:
            
            messages.error(request, f"Failed to fetch calorie information. Status Code: {response.status_code}")
    
    
    return render(request, 'calorie_tracker/add_food_item.html', {'form': form})
# view for deleting food item
def delete_food_item(request, pk):
    FoodItem.objects.filter(id=pk).delete()
    return redirect('food_item_list')
#view for sugest recipe
def suggest_recipe(request):
    form = IngredientForm()
    recipes = []
    error_message = None

    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            # Split the ingredients string by commas and strip whitespace
            ingredients = [ingredient.strip() for ingredient in form.cleaned_data['ingredients'].split(',')]
            # Create a query string with multiple 'ingredients' parameters
            query_params = '&'.join([f'ingredients={ingredient}' for ingredient in ingredients])
            api_url = f"http://recipe-apii-env.eba-x2cwht2h.us-east-1.elasticbeanstalk.com/api/recipes/search?{query_params}"
            response = requests.get(api_url)
            
            if response.status_code == 200:
                recipes_data = response.json()
                # include the recipe name and instructions in the response
                recipes = [{'name': recipe['name'], 'instructions': recipe['instructions']} for recipe in recipes_data]
            else:
                error_message = "Failed to fetch recipes. Please try again later."

    return render(request, 'calorie_tracker/suggest_recipe.html', {
        'form': form, 'recipes': recipes, 'error_message': error_message
    })

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
                
            else:
                
                pass  
    else:
        form = CalorieIntakeForm()
        recommended_intake = None  


    return render(request, 'calorie_tracker/calorie_intake.html', {'form': form, 'recommended_intake': recommended_intake})