from django.contrib import admin
from .models import Ingredient

# class IngredientAdmin(admin.ModelAdmin):
#     fields = 


admin.site.register(Ingredient)