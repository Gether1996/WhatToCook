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
from viewer.views import logout_view, registration, main_meal_categories, secondary_meal_categories, filtered_meals, ingredient_categories, ingredients
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
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
