from django.shortcuts import render, redirect
from django.contrib.auth import logout
from viewer.forms import SignUpForm
from viewer.models import MainMealCategory, SecondaryMealCategory, Meal


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


def meals_in_sec_category(request, secondary_category_id):
    meals = Meal.objects.filter(category=secondary_category_id)
    return render(request, 'filtered_meals.html', {'meals': meals})