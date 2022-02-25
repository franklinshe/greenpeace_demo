# Generated by Django 3.1.7 on 2021-05-03 20:49

import database.models
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default=None, max_length=50)),
                ('start_date', models.DateField(blank=True, default=None)),
                ('end_date', models.DateField(blank=True, default=None)),
                ('NRO', models.CharField(blank=True, default=None, max_length=50)),
                ('evaluator', models.CharField(blank=True, default=None, max_length=50)),
                ('cause_area', models.CharField(blank=True, default=None, max_length=50)),
                ('keywords', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, default=None, max_length=20), default=database.models.Evaluation.get_default_keywords, size=50)),
                ('executive_summary', models.TextField(blank=True, default=None)),
                ('link', models.CharField(blank=True, default=None, max_length=200)),
                ('embed_link', models.CharField(blank=True, default=None, max_length=200)),
            ],
        ),
    ]