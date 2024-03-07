# Generated by Django 5.0.3 on 2024-03-07 10:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('importance', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('TaskMade', models.DateTimeField(default=datetime.datetime(2024, 3, 7, 11, 39, 2, 394134))),
                ('TaskDue', models.CharField(max_length=100)),
            ],
        ),
    ]