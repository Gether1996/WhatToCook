"""
URL configuration for WhatToCook project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from viewer.views import homepage
from django.urls import path, include
from viewer.views import logout_view, registration, main_meal_categories, secondary_meal_categories, \
    filtered_meals, ingredient_categories, ingredients, meal_detail, favorite_meals_for_user, create_favorite_meal, \
    delete_favorite_meal
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    path('accounts/logout/', logout_view),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registration/', registration, name='registration'),
    path('accounts/profile/', homepage, name='profile'),
    path('main_meal_categories/', main_meal_categories, name='main_meal_categories'),
    path('secondary_meal_categories/<int:main_category_id>/', secondary_meal_categories, name='secondary_meal_categories'),
    path('filtered_meals/ingredient/<int:ingredient_id>/', filtered_meals, name='filtered_meals_by_ingredient'),
    path('filtered_meals/category/<int:secondary_category_id>/', filtered_meals, name='filtered_meals_by_category'),
    path('ingredient_categories/', ingredient_categories, name='ingredient_categories'),
    path('ingredients/<int:category_id>/', ingredients, name='ingredients'),
    path('meal_detail/<int:meal_id>/', meal_detail, name='meal_detail'),
    path('favorite_meals/', favorite_meals_for_user, name="favorite_meals_for_user"),
    path('create_favorite_meal/<int:meal_id>/', create_favorite_meal, name='create_favorite_meal'),
    path('delete_favorite_meal/<int:favorite_meal_id>/', delete_favorite_meal, name='delete_favorite_meal'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
