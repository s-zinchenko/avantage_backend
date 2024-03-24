# Generated by Django 5.0.3 on 2024-03-23 09:07

import utils.files
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='galleryattachment',
            options={'verbose_name': 'Вложение галереи', 'verbose_name_plural': 'Вложения галереи'},
        ),
        migrations.AlterField(
            model_name='award',
            name='attachment',
            field=models.FileField(upload_to=utils.files.upload_path, verbose_name='ЗD модель награды'),
        ),
        migrations.AlterField(
            model_name='company',
            name='about_image',
            field=models.FileField(upload_to=utils.files.upload_path, verbose_name='Изображение о компании'),
        ),
        migrations.AlterField(
            model_name='company',
            name='agreement',
            field=models.FileField(upload_to=utils.files.upload_path, verbose_name='Согласие на обработку персональных данных'),
        ),
        migrations.AlterField(
            model_name='company',
            name='brief',
            field=models.FileField(upload_to=utils.files.upload_path, verbose_name='Бриф'),
        ),
        migrations.AlterField(
            model_name='company',
            name='form_for_freelancers',
            field=models.FileField(upload_to=utils.files.upload_path, verbose_name='Форма для фрилансеров'),
        ),
        migrations.AlterField(
            model_name='company',
            name='intro_video',
            field=models.FileField(upload_to=utils.files.upload_path, verbose_name='Видео'),
        ),
        migrations.AlterField(
            model_name='company',
            name='portfolio',
            field=models.FileField(upload_to=utils.files.upload_path, verbose_name='Портфолио'),
        ),
        migrations.AlterField(
            model_name='company',
            name='presentation',
            field=models.FileField(upload_to=utils.files.upload_path, verbose_name='Презентация'),
        ),
        migrations.AlterField(
            model_name='company',
            name='requisites',
            field=models.FileField(upload_to=utils.files.upload_path, verbose_name='Реквизиты'),
        ),
        migrations.AlterField(
            model_name='galleryattachment',
            name='image',
            field=models.FileField(upload_to=utils.files.upload_path, verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='photo',
            field=models.FileField(upload_to=utils.files.upload_path, verbose_name='Фото'),
        ),
    ]
