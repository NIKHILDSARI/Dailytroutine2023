# Generated by Django 4.1.7 on 2023-03-02 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Foodroutine', '0010_meallog_remove_dinnerlog_user_remove_lunchlog_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meallog',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='meallog',
            name='time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
