from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from ussr import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'recipes', views.RecipeViewSet)
router.register(r'reviews', views.ReviewViewSet)
router.register(r'recipe-rates', views.RecipeRateViewSet)
router.register(r'review-rates', views.ReviewRateViewSet)
router.register(r'bookmarks', views.BookmarksViewSet)
router.register(r'ingredients', views.IngredientViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('admin', admin.site.urls)
]
