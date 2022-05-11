from statistics import mode
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User as BaseUser
'''Чекайте модель базы данных, которую делал Артём (важная заметочка)'''

class User(BaseUser):
    level = models.CharField('Уровень пользователя', max_length=255) # Чекайте систему рангов


class Ingredient(models.Model):
    name = models.CharField('название', max_length=255)
    calories = models.FloatField('калорий на 100г', blank=True)
    proteins = models.FloatField('белков на 100г', blank=True)
    fats = models.FloatField('жиров на 100г', blank=True)
    carbohydrates = models.FloatField('углеводов на 100г', blank=True)
    type = models.CharField('тип продукта \n(например, для помидора: "Черри")', max_length=255, blank=True)

    def __str__(self) -> str:
        return self.get_full_name()

    def get_full_name(self) -> str:
        return self.name + self.type if self.type is not None else self.name

    class Meta:
        verbose_name = 'ингредиент'
        verbose_name_plural = 'ингредиенты'

class Recipe(models.Model):
    name = models.CharField('название рецепта', max_length=255)
    text = models.TextField('текст рецепта', max_length=10000)
    cooking_time = models.TimeField('время готовки', default='00:05', blank=True)
    photo = models.ImageField('фото рецепта', upload_to='recipes/images', blank=True)
    video = models.FileField('видео рецепта', upload_to='recipes/videos', blank=True)
    country = models.CharField('страна происхождения рецепта', max_length=255, blank=True)
    type = models.CharField('тип блюда', max_length=255) # Such as Борщи, Амогусы
    cooking_type = models.CharField('тип приготовления', max_length=255) # Such as Жарка, Варка
    create_datetime = models.DateTimeField('время создания', auto_now_add=True)
    last_edited_datetime = models.DateTimeField('время последнего изменения', auto_now=True)


class Review(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE, verbose_name='рецепт, на который был оставлен коммент')
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='пользователь, оставивший отзыв')
    text = models.TextField('текст отзыва')
    create_datetime = models.DateTimeField('время создания', auto_now_add=True)
    # rate = models.ManyToManyField(User)
    # TODO: Узнать как тут нормально реализовать многие ко многим и сделать


class Bookmarks(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    create_datetime = models.DateTimeField('дата создания', auto_now_add=True)


class Composition(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.SET_NULL, blank=True, null=True)
    volume = models.CharField('количество / вес', max_length=255, blank=True)
    is_required = models.BooleanField('обязательный ингредиент', default=False)
    type_is_required = models.BooleanField('обязательный тип ингредиента', default=False)
