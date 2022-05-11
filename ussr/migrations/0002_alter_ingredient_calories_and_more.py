# Generated by Django 4.0.4 on 2022-05-11 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ussr', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='calories',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='carbohydrates',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='fats',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='proteins',
            field=models.FloatField(blank=True),
        ),
    ]
