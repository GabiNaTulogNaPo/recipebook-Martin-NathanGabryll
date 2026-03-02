from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Recipe, Ingredient, RecipeIngredient, Profile


# Register your models here.
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(admin.BaseUserAdmin):
    inlines = [ProfileInline,]


class InlineRecipeIngredient(admin.TabularInline):
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [InlineRecipeIngredient]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Ingredient)
admin.site.register(Recipe, RecipeAdmin)
