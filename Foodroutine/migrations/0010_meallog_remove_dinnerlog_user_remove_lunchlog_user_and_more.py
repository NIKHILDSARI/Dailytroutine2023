# Generated by Django 4.1.7 on 2023-03-02 04:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Foodroutine', '0009_alter_breakfastlog_breakfast_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meallog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(auto_created=True)),
                ('date', models.DateField(auto_created=True)),
                ('username', models.CharField(blank=True, max_length=200, null=True)),
                ('meal_name', models.CharField(blank=True, max_length=200, null=True)),
                ('meal_recipe', models.TextField(blank=True, null=True)),
                ('calories', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='dinnerlog',
            name='user',
        ),
        migrations.RemoveField(
            model_name='lunchlog',
            name='user',
        ),
        migrations.RemoveField(
            model_name='snackslog',
            name='user',
        ),
        migrations.DeleteModel(
            name='BreakfastLog',
        ),
        migrations.DeleteModel(
            name='dinnerlog',
        ),
        migrations.DeleteModel(
            name='Lunchlog',
        ),
        migrations.DeleteModel(
            name='Snackslog',
        ),
    ]
