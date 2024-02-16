# Generated by Django 5.0.2 on 2024-02-16 15:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Segment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'segment',
                'verbose_name_plural': 'segmenti',
                'ordering': ('naziv',),
            },
        ),
        migrations.CreateModel(
            name='Ptica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('slika', models.ImageField(blank=True, upload_to='ptice/%Y/%m/%d')),
                ('opis', models.TextField(blank=True)),
                ('cena', models.DecimalField(decimal_places=2, max_digits=10)),
                ('raspoloziv', models.BooleanField(default=True)),
                ('kreiran', models.DateTimeField(auto_now_add=True)),
                ('azuriran', models.DateTimeField(auto_now=True)),
                ('segment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ptice', to='SalonPtica.segment')),
            ],
            options={
                'verbose_name_plural': 'ptice',
                'ordering': ('naziv',),
                'index_together': {('id', 'slug')},
            },
        ),
    ]
