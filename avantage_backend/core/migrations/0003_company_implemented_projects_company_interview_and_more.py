# Generated by Django 5.0.3 on 2024-03-23 10:49

import utils.files
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_galleryattachment_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='implemented_projects',
            field=models.PositiveIntegerField(default=1, verbose_name='Реализованных проектов'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='interview',
            field=models.FileField(default='None', upload_to=utils.files.upload_path, verbose_name='Презентация о компании'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='unique_scenarios',
            field=models.PositiveIntegerField(default=1, verbose_name='Уникальных сценарии'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='welcome_video',
            field=models.FileField(default='None', upload_to=utils.files.upload_path, verbose_name='Приветственное видео'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='years_of_experience',
            field=models.PositiveIntegerField(default=1, verbose_name='Годы опыта'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='intro_video',
            field=models.FileField(upload_to=utils.files.upload_path, verbose_name='Шоурил'),
        ),
    ]
