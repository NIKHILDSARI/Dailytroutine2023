# Generated by Django 4.1.7 on 2023-03-09 14:43

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userAuth', '0002_message_to_you_visite_delete_message_to_nikhil_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message_to_you',
            name='Message',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
