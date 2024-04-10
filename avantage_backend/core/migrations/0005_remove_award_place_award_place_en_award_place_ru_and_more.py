# Generated by Django 5.0.3 on 2024-04-10 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_teammember_is_chief"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="award",
            name="place",
        ),
        migrations.AddField(
            model_name="award",
            name="place_en",
            field=models.CharField(
                max_length=256, null=True, verbose_name="Место (En)"
            ),
        ),
        migrations.AddField(
            model_name="award",
            name="place_ru",
            field=models.CharField(
                max_length=256, null=True, verbose_name="Место (Ru)"
            ),
        ),
        migrations.AlterField(
            model_name="teammember",
            name="is_chief",
            field=models.BooleanField(
                default=False, verbose_name="Руководитель?"
            ),
        ),
    ]