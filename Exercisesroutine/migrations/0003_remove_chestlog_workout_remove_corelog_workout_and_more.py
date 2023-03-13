# Generated by Django 4.1.7 on 2023-02-28 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exercisesroutine', '0002_backlog_set1_weight_inkg_backlog_set2_weight_inkg_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chestlog',
            name='workout',
        ),
        migrations.RemoveField(
            model_name='corelog',
            name='workout',
        ),
        migrations.RemoveField(
            model_name='leglog',
            name='workout',
        ),
        migrations.RemoveField(
            model_name='shoulderlog',
            name='workout',
        ),
        migrations.RemoveField(
            model_name='workoutlog',
            name='bodypart',
        ),
        migrations.AddField(
            model_name='workoutlog',
            name='bodypary',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='workoutlog',
            name='exercises',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='workoutlog',
            name='set1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='workoutlog',
            name='set1_weight_inkg',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='workoutlog',
            name='set2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='workoutlog',
            name='set2_weight_inkg',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='workoutlog',
            name='set3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='workoutlog',
            name='set3_weight_inkg',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='workoutlog',
            name='set4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='workoutlog',
            name='set4_weight_inkg',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Backlog',
        ),
        migrations.DeleteModel(
            name='Chestlog',
        ),
        migrations.DeleteModel(
            name='Corelog',
        ),
        migrations.DeleteModel(
            name='Leglog',
        ),
        migrations.DeleteModel(
            name='Shoulderlog',
        ),
    ]