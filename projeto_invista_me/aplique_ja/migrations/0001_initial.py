# Generated by Django 5.1.4 on 2024-12-15 02:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.TextField(max_length=255)),
                ('valor', models.FloatField()),
                ('pago', models.BooleanField(default=False)),
                ('date', models.DateField(default=datetime.datetime.now)),
            ],
        ),
    ]
