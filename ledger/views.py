from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Recipe
from .forms import RecipeForm

def recipe_list(request):
    recipes = Recipe.objects.all()
    context = {"recipes": recipes}
    return render(request, "recipe_list.html", context)

@login_required
def recipe_detail(request, id):
    context = {'recipe': Recipe.objects.get(id=id)}
    return render(request, "recipe_template.html", context)

@login_required
def recipe_add(request):
    form = RecipeForm()
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ledger:recipe_list')
    context = {"form": form}
    return render(request, "recipe_add.html", context)



