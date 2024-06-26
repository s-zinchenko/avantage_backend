# Generated by Django 5.0.3 on 2024-03-23 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_ru', models.CharField(max_length=512, verbose_name='Название услуги (Ru)')),
                ('title_en', models.CharField(max_length=512, verbose_name='Название услуги (En)')),
                ('description_ru', models.CharField(max_length=1024, verbose_name='Описание (Ru)')),
                ('description_en', models.CharField(max_length=1024, verbose_name='Описание (En)')),
                ('order', models.PositiveIntegerField(verbose_name='Порядковый номер')),
                ('external_link', models.URLField(blank=True, max_length=512, null=True, verbose_name='Ссылка')),
                ('events_ru', models.TextField(verbose_name='События (Ru)')),
                ('events_en', models.TextField(verbose_name='События (En)')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
    ]
