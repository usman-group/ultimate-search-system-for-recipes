from django.contrib.auth.models import User as DjangoUser
from django.contrib.auth.models import Group
from .models import *
from rest_framework import viewsets
from .serializers import *


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DjangoUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class BookmarksViewSet(viewsets.ModelViewSet):
    queryset = Bookmarks.objects.all()
    serializer_class = BookmarksSerializer


class CompositionViewSet(viewsets.ModelViewSet):
    queryset = Composition.objects.all()
    serializer_class = CompositionSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewRateViewSet(viewsets.ModelViewSet):
    queryset = ReviewRate.objects.all()
    serializer_class = ReviewRateSerializer


class RecipeRateViewSet(viewsets.ModelViewSet):
    queryset = RecipeRate.objects.all()
    serializer_class = RecipeRateSerializer
