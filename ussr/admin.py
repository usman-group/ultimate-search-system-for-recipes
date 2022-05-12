from django.contrib import admin
from .models import *


class RecipeAdmin(admin.ModelAdmin):
    readonly_fields=['create_datetime', 'last_edited_datetime', 'average_rate']



admin.site.register(Composition)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(User)
admin.site.register(Review)
admin.site.register(ReviewRate)
admin.site.register(RecipeRate)
admin.site.register(Bookmarks)
admin.site.register(Ingredient)