# Generated by Django 4.0.6 on 2024-05-06 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0002_letter_lang'),
    ]

    operations = [
        migrations.AddField(
            model_name='letter',
            name='site_lang',
            field=models.CharField(choices=[('ru', 'Ru'), ('en', 'En')], default='ru', max_length=32, null=True, verbose_name='Язык сайта'),
        ),
    ]
