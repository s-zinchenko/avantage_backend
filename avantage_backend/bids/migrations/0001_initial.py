# Generated by Django 5.0.3 on 2024-03-23 08:49

import avantage_backend.bids.mixins
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CooperationBid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=512, verbose_name='Полное имя')),
                ('contact_phone', models.CharField(max_length=32, verbose_name='Контактный телефон')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('project_scope', models.TextField(blank=True, null=True, verbose_name='Сфера проекта')),
                ('project_goals', models.TextField(verbose_name='Цели и задачи проекта')),
            ],
            options={
                'verbose_name': 'Заявка на сотрудничество',
                'verbose_name_plural': 'Заявки на сотрудничество',
            },
            bases=(avantage_backend.bids.mixins.SendEmailMixin, models.Model),
        ),
    ]
