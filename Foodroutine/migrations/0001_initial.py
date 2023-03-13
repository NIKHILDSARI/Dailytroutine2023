# Generated by Django 4.1.7 on 2023-02-22 06:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Targetfoodroutine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breakfast', models.TextField()),
                ('breakfastcalories', models.IntegerField()),
                ('lunch', models.TextField()),
                ('lunchfastcalories', models.IntegerField()),
                ('dinner', models.TextField()),
                ('dinnercalories', models.IntegerField()),
                ('snacks', models.TextField()),
                ('snackscalories', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FoodLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breakfast', models.TextField()),
                ('breakfastcalories', models.IntegerField()),
                ('lunch', models.TextField()),
                ('lunchfastcalories', models.IntegerField()),
                ('dinner', models.TextField()),
                ('dinnercalories', models.IntegerField()),
                ('snacks', models.TextField()),
                ('snackscalories', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
