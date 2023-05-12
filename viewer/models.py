from django.db.models import *
from django.core.validators import MinValueValidator


class IngredientCategory(Model):
    name = CharField(max_length=50)

    def __str__(self):
        return self.name

# Meat (including beef, pork, lamb, poultry, game meat, and more)
# Seafood (including fish, shellfish, and crustaceans)
# Dairy products (including milk, cheese, yogurt, and butter)
# Eggs
# Vegetables (including leafy greens, root vegetables, cruciferous vegetables, and more)
# Fruits (including berries, citrus fruits, tropical fruits, and more)
# Grains (including wheat, rice, oats, corn, and more)
# Legumes (including beans, lentils, chickpeas, and more)
# Nuts and seeds (including almonds, cashews, sunflower seeds, and more)
# Oils and fats (including olive oil, coconut oil, butter, and more)


class Ingredient(Model):
    name = CharField(max_length=50)
    category = ForeignKey(IngredientCategory, on_delete=CASCADE)
    calories_per_100g = IntegerField(validators=[MinValueValidator(1)], blank=False)

    def __str__(self):
        return self.name


class MealCategory(Model):
    name = CharField(max_length=50)


class Meal(Model):
    name = CharField(max_length=50)
    category = ForeignKey(MealCategory, on_delete=CASCADE)
    ingredients = ManyToManyField(Ingredient)
    description = TextField()
    recipe_text = TextField()
    picture = ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.name


