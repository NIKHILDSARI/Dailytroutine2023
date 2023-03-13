from django.forms import ModelForm,Form
from django import forms
from .models import *
from django.core.exceptions import ValidationError


class SettargetFoodroutineform(forms.Form):

    Meal_Recipe = forms.CharField(widget=forms.Textarea,required=True)

    Meal_calories = forms.IntegerField(required=True)



    

class Meallogform(forms.Form):

    Meal_Recipe = forms.CharField(widget=forms.Textarea,required=True)

    Meal_calories = forms.IntegerField(required=True)



