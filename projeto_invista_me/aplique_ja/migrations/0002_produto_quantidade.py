# Generated by Django 5.1.4 on 2024-12-15 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplique_ja', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='quantidade',
            field=models.IntegerField(default=1),
        ),
    ]
