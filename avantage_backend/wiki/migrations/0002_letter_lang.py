# Generated by Django 5.0.3 on 2024-04-14 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wiki", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="letter",
            name="lang",
            field=models.CharField(
                choices=[("ru", "Ru"), ("en", "En")],
                max_length=32,
                null=True,
                verbose_name="Язык",
            ),
        ),
    ]
