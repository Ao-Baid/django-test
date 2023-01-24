# Generated by Django 4.1.5 on 2023-01-19 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.CharField(blank=True, choices=[('en', 'English'), ('fr', 'French'), ('es', 'Spanish'), ('it', 'Italian'), ('de', 'German'), ('ru', 'Russian'), ('zh', 'Chinese'), ('ja', 'Japanese'), ('ko', 'Korean'), ('ar', 'Arabic')], default='en', help_text='Book language', max_length=3),
        ),
    ]