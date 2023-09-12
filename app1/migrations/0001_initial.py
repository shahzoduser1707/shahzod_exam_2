# Generated by Django 4.2.5 on 2023-09-12 09:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ustalar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usta_name', models.CharField(default='', max_length=150)),
                ('order_name', models.CharField(default='', max_length=200)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField(default=datetime.datetime.now)),
                ('status', models.BooleanField(default=False)),
                ('description', models.TextField(verbose_name='you can type anything')),
            ],
        ),
    ]
