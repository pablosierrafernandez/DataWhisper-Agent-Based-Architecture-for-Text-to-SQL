# Generated by Django 5.1 on 2024-08-20 19:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('business_value', models.TextField()),
                ('sql', models.TextField()),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='insights', to='chat.message')),
            ],
        ),
    ]