# Generated by Django 5.0.6 on 2024-06-04 15:47

import utils.files
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0013_alter_award_options_remove_award_case_link_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="company",
            name="about_image",
        ),
        migrations.RemoveField(
            model_name="company",
            name="about_text_en",
        ),
        migrations.RemoveField(
            model_name="company",
            name="about_text_ru",
        ),
        migrations.RemoveField(
            model_name="company",
            name="greeting_description_en",
        ),
        migrations.RemoveField(
            model_name="company",
            name="greeting_description_ru",
        ),
        migrations.RemoveField(
            model_name="company",
            name="greeting_title_en",
        ),
        migrations.RemoveField(
            model_name="company",
            name="greeting_title_ru",
        ),
        migrations.AlterField(
            model_name="company",
            name="interview",
            field=models.FileField(
                upload_to=utils.files.upload_path,
                verbose_name="Презентация о компании (Интервью)",
            ),
        ),
        migrations.AlterField(
            model_name="company",
            name="welcome_video",
            field=models.FileField(
                upload_to=utils.files.upload_path,
                verbose_name="Приветственное видео (В кружке)",
            ),
        ),
    ]
