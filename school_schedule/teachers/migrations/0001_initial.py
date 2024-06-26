# Generated by Django 5.0.6 on 2024-05-18 10:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to='subjects.subject')),
            ],
        ),
    ]
