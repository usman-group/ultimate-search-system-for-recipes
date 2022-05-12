from django.contrib import admin
from .models import *

admin.site.register(Composition)
admin.site.register(Recipe)
admin.site.register(User)
admin.site.register(Review)
admin.site.register(ReviewRate)
admin.site.register(RecipeRate)
admin.site.register(Bookmarks)
admin.site.register(Ingredient)