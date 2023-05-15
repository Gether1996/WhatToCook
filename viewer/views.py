from django.shortcuts import render, redirect
from django.contrib.auth import logout
from viewer.forms import SignUpForm
from viewer.models import MainMealCategory, SecondaryMealCategory, Meal, IngredientCategory, Ingredient
import random


def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = SignUpForm()
    return render(request, 'registration.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('homepage')


def homepage(request):
    context = {
    }
    return render(request, 'homepage.html', context)


def main_meal_categories(request):
    main_categories = MainMealCategory.objects.all()
    return render(request, 'main_meal_categories.html', {'main_categories': main_categories})


def secondary_meal_categories(request, main_category_id):
    secondary_categories = SecondaryMealCategory.objects.filter(main_category=main_category_id)
    return render(request, 'secondary_meal_categories.html', {'secondary_categories': secondary_categories})


def filtered_meals(request, ingredient_id=None, secondary_category_id=None):
    if ingredient_id:
        meals = Meal.objects.filter(ingredients=ingredient_id)
    elif secondary_category_id:
        meals = Meal.objects.filter(category=secondary_category_id)
    else:
        meals = Meal.objects.all()
    return render(request, 'filtered_meals.html', {'meals': meals})


def ingredient_categories(request):
    ingredient_category = IngredientCategory.objects.all()
    return render(request, 'ingredient_categories.html', {'ingredient_category': ingredient_category})


def ingredients(request, category_id):
    ingredients = Ingredient.objects.filter(category__id=category_id)
    for ingredient in ingredients:
        ingredient.color_r, ingredient.color_g, ingredient.color_b = 60, 60, 60
    return render(request, 'ingredients.html', {'ingredients': ingredients})
