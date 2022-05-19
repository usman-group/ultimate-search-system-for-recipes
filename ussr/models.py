from django.db import models
from django.core import validators
from django.contrib.auth.models import User as BaseUser

'''
Чекайте модель базы данных, которую делал Артём (важная заметочка)
'''


class User(BaseUser):
    level = models.CharField('Уровень пользователя', max_length=255)  # Чекайте систему рангов


class Ingredient(models.Model):
    name = models.CharField('название', max_length=255)
    calories = models.FloatField('килокалорий на 100г', blank=True)
    proteins = models.FloatField('белков на 100г', blank=True)
    fats = models.FloatField('жиров на 100г', blank=True)
    carbohydrates = models.FloatField('углеводов на 100г', blank=True)
    type = models.CharField('тип продукта (например, для помидора: "Черри")', max_length=255, blank=True)

    def __str__(self) -> str:
        return self.get_full_name()

    def get_full_name(self) -> str:
        return f'{self.name} {self.type}' if self.type is not None else self.name

    class Meta:
        verbose_name = 'ингредиент'
        verbose_name_plural = 'ингредиенты'


class Recipe(models.Model):
    name = models.CharField('название рецепта', max_length=255)
    text = models.TextField('текст рецепта', max_length=10000)
    cooking_time = models.TimeField('время готовки чч:мм:сс', default='00:05', blank=True)
    photo = models.ImageField('фото рецепта', upload_to='recipes/images', blank=True)
    video = models.FileField('видео рецепта', upload_to='recipes/videos', blank=True)
    country = models.CharField('страна происхождения рецепта', max_length=255, blank=True)
    type = models.CharField('тип блюда', max_length=255)  # Such as Борщи, Амогусы
    # TODO: Выяснить нужно ли поле cooking_type (Салаты всегда салаты, а борщи всегда варить)
    cooking_type = models.CharField('тип приготовления', max_length=255)  # Such as Жарка, Варка
    create_datetime = models.DateTimeField('время создания', auto_now_add=True)
    last_edited_datetime = models.DateTimeField('время последнего изменения', auto_now=True)
    average_rate = models.PositiveSmallIntegerField(
        'средняя оценка', validators=[validators.MaxValueValidator(10)], null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'рецептик'
        verbose_name_plural = 'рецептики'


class Review(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, verbose_name='рецепт, на который был оставлен коммент')
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='пользователь, оставивший отзыв'
    )
    text = models.TextField('текст отзыва')
    create_datetime = models.DateTimeField('время создания', auto_now_add=True)
    average_rate = models.PositiveIntegerField(
        'средняя оценка отзыва', validators=[validators.MaxValueValidator(10)], null=True, blank=True
    )

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'


class ReviewRate(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, verbose_name='отзыв, на который поставлена оценка')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь, поставивший оценку')
    average_rate = models.PositiveSmallIntegerField(
        'оценка отзыва от 1 до 10', validators=[validators.MaxValueValidator(10)], null=True, blank=True
    )
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['review_id', 'user_id'], name='unique_reviewid-userid_reviewrate')
        ]
        verbose_name = 'оценка отзыва'
        verbose_name_plural = 'оценки отзывов'


class RecipeRate(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, verbose_name='рецепт, на который поставлена оценка')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь, поставивший оценку')
    rate = models.PositiveSmallIntegerField('оценка рецепта от 1 до 10', validators=[validators.MaxValueValidator(10)])
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['recipe_id', 'user_id'], name='unique_recipeid-userid_reciperate')
        ]
        verbose_name = 'оценка рецепта'
        verbose_name_plural = 'оценки рецептов'


class Bookmarks(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_datetime = models.DateTimeField('дата создания', auto_now_add=True)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['recipe_id', 'user_id'], name='unique_recipeid-userid_bookmarks')
        ]
        verbose_name = 'заметка'
        verbose_name_plural = 'заметки'


class Composition(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, verbose_name='рецептик')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, verbose_name='ингредиент')
    volume = models.CharField('количество / вес', max_length=255, blank=True)
    is_required = models.BooleanField('обязательный ингредиент', default=False)
    type_is_required = models.BooleanField('обязательный тип ингредиента', default=False)

    def __str__(self) -> str:
        return f'{self.recipe_id}, {self.ingredient_id}'

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['recipe_id', 'ingredient_id'], name='unique_recipeid-ingredientid_composition'
            )
        ]
        verbose_name = 'состав'
        verbose_name_plural = 'составы'


class TypeDish(models.Model):