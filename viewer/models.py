from django.db.models import *
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User


class IngredientCategory(Model):
    name = CharField(max_length=50)

    def __str__(self):
        return self.name


class Ingredient(Model):
    name = CharField(max_length=50)
    category = ForeignKey(IngredientCategory, on_delete=CASCADE)
    calories_per_100g = IntegerField(validators=[MinValueValidator(1)], blank=False)

    def __str__(self):
        return f"{self.name} ({self.category})"


class MainMealCategory(Model):
    name = CharField(max_length=50)

    def __str__(self):
        return self.name


class SecondaryMealCategory(Model):
    name = CharField(max_length=50)
    main_category = ForeignKey(MainMealCategory, on_delete=CASCADE)

    def __str__(self):
        return f"{self.name} ({self.main_category})"


class Meal(Model):
    name = CharField(max_length=50)
    category = ManyToManyField(SecondaryMealCategory)
    ingredients = ManyToManyField(Ingredient)
    description = TextField()
    recipe_text = TextField()
    picture = ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.name


class FavoriteMeal(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    meal = ForeignKey(Meal, on_delete=CASCADE)


