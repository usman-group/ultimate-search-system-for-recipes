from django.db import models
from django.contrib.auth.models import User as BaseUser
'''Чекайте модель базы данных, которую делал Артём (важная заметочка)'''

class User(BaseUser):
    level = models.CharField() # Чекайте систему рангов


class Ingredient:
    name = models.CharField(max_length=255)
    calories = models.IntegerField(blank=True)
    proteins = models.IntegerField(blank=True)
    fats = models.IntegerField(blank=True)
    carbohydrates = models.IntegerField(blank=True)
    type = models.CharField(max_length=255, blank=True)
    type_is_required = models.BooleanField(default=False)

    def get_full_name(self):
        return self.name + self.type if self.type is not None else self.name


class Recipe:
    name = models.CharField('Название рецепта', max_length=255)
    text = models.TextField('Текст рецепта', max_length=10000)
    cooking_time = models.TimeField('Время готовки', default='00:05', blank=True)
    photo = models.ImageField('Фото рецепта', upload_to='recipes/images', blank=True)
    video = models.FileField('Видео рецепта', upload_to='recipes/videos', blank=True)
    country = models.CharField('Страна происхождения рецепта', max_length=255, blank=True)
    type = models.CharField('Тип блюда', max_length=255) # Such as Борщи, Амогусы
    cooking_type = models.CharField('Тип приготовления', max_length=255) # Such as Жарка, Варка
    create_datetime = models.DateTimeField('Время создания', auto_now_add=True)
    last_edited_datetime = models.DateTimeField('Время последнего изменения', auto_now=True)


class Review:
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    #TODO: Доделать модели