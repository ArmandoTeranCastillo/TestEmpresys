# Generated by Django 4.1.3 on 2022-11-10 00:43

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='census',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('state_title', models.CharField(max_length=50)),
                ('census', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='graph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('x_axis_title', models.CharField(max_length=50)),
                ('y_axis_title', models.CharField(max_length=50)),
                ('x_axis_range', django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(decimal_places=2, max_digits=10), blank=True, size=2)),
                ('y_axis_range', django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(decimal_places=2, max_digits=10), blank=True, size=2)),
                ('year_range', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, null=True), blank=True, size=2)),
            ],
        ),
    ]
