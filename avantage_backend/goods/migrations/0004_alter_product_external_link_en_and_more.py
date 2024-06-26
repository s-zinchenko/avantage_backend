# Generated by Django 4.0.6 on 2024-04-25 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_rename_external_link_product_external_link_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='external_link_en',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='Ссылка (En)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='external_link_ru',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='Ссылка (Ru)'),
        ),
    ]
