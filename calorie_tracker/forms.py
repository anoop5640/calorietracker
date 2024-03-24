from django import forms
from .models import FoodItem

class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ['name'] # Only include the 'name' field


class IngredientForm(forms.Form):
    ingredients = forms.CharField(label='Enter Ingredients', max_length=100,
                                  help_text='Enter ingredients separated by commas (e.g., chicken, potato)')
