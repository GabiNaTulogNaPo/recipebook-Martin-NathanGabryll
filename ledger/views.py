from django.shortcuts import render
from .models import Recipe

def recipe_list(request):
    recipes = Recipe.objects.all()
    context = {"recipes": recipes}
    return render(request, "recipe_list.html", context)

def recipe_detail(request, id):
    context = {'recipe': Recipe.objects.get(id=id)}
    return render(request, "recipe_template.html", context)

