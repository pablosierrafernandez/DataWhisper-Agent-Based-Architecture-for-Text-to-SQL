# Generated by Django 5.1 on 2024-08-21 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_insight'),
    ]

    operations = [
        migrations.AddField(
            model_name='apiconfiguration',
            name='num_insights',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='apiconfiguration',
            name='opcion',
            field=models.BooleanField(default=False),
        ),
    ]