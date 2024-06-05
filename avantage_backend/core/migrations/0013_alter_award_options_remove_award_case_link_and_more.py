# Generated by Django 5.0.6 on 2024-06-02 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0012_remove_award_case_award_case_link"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="award",
            options={
                "ordering": ["award_order"],
                "verbose_name": "Награда",
                "verbose_name_plural": "Награды",
            },
        ),
        migrations.RemoveField(
            model_name="award",
            name="case_link",
        ),
        migrations.AddField(
            model_name="award",
            name="case_link_en",
            field=models.CharField(
                max_length=1024, null=True, verbose_name="Ссылка на кейс (En)"
            ),
        ),
        migrations.AddField(
            model_name="award",
            name="case_link_ru",
            field=models.CharField(
                max_length=1024, null=True, verbose_name="Ссылка на кейс (Ru)"
            ),
        ),
    ]