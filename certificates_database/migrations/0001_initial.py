# Generated by Django 3.2.12 on 2022-03-07 22:57

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminIP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('nationality', models.CharField(max_length=255, null=True)),
                ('birth_date', models.DateField()),
                ('subject', models.CharField(max_length=255)),
                ('achievement_date', models.DateField()),
                ('certificate_score', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(30), django.core.validators.MinValueValidator(0)])),
                ('issuance_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('hash', models.CharField(blank=True, default=None, max_length=66, null=True)),
                ('txId', models.CharField(blank=True, default=None, max_length=66, null=True)),
            ],
        ),
    ]
