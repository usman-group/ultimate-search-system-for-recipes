# Generated by Django 4.0.4 on 2022-05-12 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ussr', '0003_reciperate_reviewrate_alter_bookmarks_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='composition',
            name='ingredient',
        ),
        migrations.AddField(
            model_name='composition',
            name='ingredient_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ussr.ingredient', verbose_name='ингредиент'),
        ),
        migrations.AlterField(
            model_name='composition',
            name='recipe_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ussr.recipe', verbose_name='рецептик'),
        ),
        migrations.AddConstraint(
            model_name='composition',
            constraint=models.UniqueConstraint(fields=('recipe_id', 'ingredient_id'), name='unique_recipeid-ingredientid_composition'),
        ),
    ]