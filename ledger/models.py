from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.TextField(blank=True)


class Ingredient(models.Model):
    name = models.CharField( max_length=50)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("ingredient_detail", args=[str(self.id)])


class Recipe(models.Model):
    name = models.CharField( max_length=50)
    author = models.ForeignKey(
        Profile,
        related_name="recipes",
        on_delete=models.CASCADE,
        null=True,
    )
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("ledger:recipe_detail", args=[str(self.id)])


class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=50)
    ingredient = models.ForeignKey(
        Ingredient, 
        related_name="recipe", 
        on_delete=models.CASCADE
        )
    recipe = models.ForeignKey(
        Recipe, 
        related_name="ingredients", 
        on_delete=models.CASCADE
        )


class RecipeImage(models.Model):
    image = models.ImageField(upload_to='images/', null = False)
    description = models.TextField(max_length=255, blank=True)
    recipe = models.ForeignKey(
        Recipe, 
        related_name="images", 
        on_delete=models.CASCADE
        )
    
