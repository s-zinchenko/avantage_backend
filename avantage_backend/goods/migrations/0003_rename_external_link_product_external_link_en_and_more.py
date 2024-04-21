# Generated by Django 4.0.6 on 2024-04-21 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_product_background_image_alter_product_external_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='external_link',
            new_name='external_link_en',
        ),
        migrations.AddField(
            model_name='product',
            name='external_link_ru',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='Ссылка'),
        ),
    ]
