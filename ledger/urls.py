from django.urls import path
from .views import recipe_list, recipe_detail
urlpatterns = [ 
    path('recipes/list/', recipe_list, name="recipe list"),
    path('recipe/<int:id>/', recipe_detail, name="recipe 1"),
]
app_name = "ledger"