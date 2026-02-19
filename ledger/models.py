from django.db import models
from django.urls import reverse

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField( max_length=50)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("ingredient_detail", args=[str(self.id)])

class Recipe(models.Model):
    name = models.CharField( max_length=50)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("ingredient_detail", args=[str(self.id)])

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=50)
    ingredient = models.ForeignKey(
        Ingredient, 
        related_name="ingredient", 
        on_delete=models.CASCADE
        )
    recipe = models.ForeignKey(
        Recipe, 
        related_name="recipe", 
        on_delete=models.CASCADE
        )
