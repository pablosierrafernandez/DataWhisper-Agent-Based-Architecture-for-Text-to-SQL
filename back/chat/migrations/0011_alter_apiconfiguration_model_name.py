# Generated by Django 5.1 on 2024-09-03 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0010_apiconfiguration_model_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiconfiguration',
            name='model_name',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
