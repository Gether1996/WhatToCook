from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from viewer.forms import SignUpForm
from viewer.models import MainMealCategory, SecondaryMealCategory, Meal, IngredientCategory, Ingredient, FavoriteMeal
from django.contrib import messages
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
    category = MainMealCategory.objects.get(id=main_category_id)
    return render(request, 'secondary_meal_categories.html', {'secondary_categories': secondary_categories, 'category': category})


def filtered_meals(request, ingredient_id=None, secondary_category_id=None, get_random_meal=False, random_favorite=False):
    category = None
    if ingredient_id:
        meals = Meal.objects.filter(ingredients=ingredient_id)
        ingredient_category = Ingredient.objects.get(id=ingredient_id)
        category = ingredient_category if ingredient_category else None
    elif secondary_category_id:
        meals = Meal.objects.filter(category=secondary_category_id)
        secondary_category = SecondaryMealCategory.objects.get(id=secondary_category_id)
        category = secondary_category if secondary_category else None
    else:
        meals = Meal.objects.all()
        category = None

    if get_random_meal:
        excluded_categories = ["Hot beverages", "Cold beverages", "Alcoholic beverages"]
        meals = meals.exclude(category__name__in=excluded_categories)
        random_meal = random.choice(meals)
        return render(request, 'filtered_meals.html', {'meals': [random_meal]})

    if random_favorite and request.user.is_authenticated:
        logged_in_user = request.user
        favorite_meals = FavoriteMeal.objects.filter(user=logged_in_user)
        if favorite_meals:
            random_favorite_meal = random.choice(favorite_meals)
            random_meal = random_favorite_meal.meal
            return render(request, 'filtered_meals.html', {'meals': [random_meal]})
        else:
            messages.warning(request, "You don't have any favorite meals!")
            return render(request, 'homepage.html', {'meals': meals})

    if random_favorite and not request.user.is_authenticated:
        messages.warning(request, "Sorry, you need to be logged in to access random favorites.")
        return render(request, 'homepage.html', {'meals': meals})

    return render(request, 'filtered_meals.html', {'meals': meals, 'category': category})


def ingredient_categories(request):
    ingredient_category = IngredientCategory.objects.all()
    return render(request, 'ingredient_categories.html', {'ingredient_category': ingredient_category})


def ingredients(request, category_id):
    ingredients = Ingredient.objects.filter(category__id=category_id)
    category = IngredientCategory.objects.get(id=category_id)
    for ingredient in ingredients:
        ingredient.color_r, ingredient.color_g, ingredient.color_b = 60, 60, 60
    return render(request, 'ingredients.html', {'ingredients': ingredients, 'category': category})


def meal_detail(request, meal_id):
    meal = get_object_or_404(Meal, id=meal_id)
    return render(request, 'meal_detail.html', {'meal': meal})


@login_required
def create_favorite_meal(request, meal_id):
    meal = get_object_or_404(Meal, id=meal_id)
    if FavoriteMeal.objects.filter(user=request.user, meal=meal).exists():
        messages.warning(request, 'This meal is already in your favorites!')
    else:
        favorite_meal = FavoriteMeal.objects.create(user=request.user, meal=meal)
        messages.success(request, 'Meal added to favorites!')
    favorite_meals = FavoriteMeal.objects.filter(user__id=request.user.id)
    return render(request, 'favorite_meals.html', {'favorite_meals': favorite_meals})


@login_required
def delete_favorite_meal(request, favorite_meal_id):
    favorite_meal = get_object_or_404(FavoriteMeal, id=favorite_meal_id)
    favorite_meal.delete()
    messages.warning(request, 'Successfully deleted!')
    favorite_meals = FavoriteMeal.objects.filter(user__id=request.user.id)
    return render(request, 'favorite_meals.html', {'favorite_meals': favorite_meals})


@login_required
def favorite_meals_for_user(request):
    favorite_meals = FavoriteMeal.objects.filter(user__id=request.user.id)
    return render(request, 'favorite_meals.html', {'favorite_meals': favorite_meals})


def search_results(request):
    query = request.GET.get('query')

    categories = SecondaryMealCategory.objects.filter(name__icontains=query)
    meals = Meal.objects.filter(name__icontains=query)
    ingredients = Ingredient.objects.filter(name__icontains=query)

    context = {
        'query': query,
        'categories': categories,
        'meals': meals,
        'ingredients': ingredients,
    }

    return render(request, 'search_results.html', context)