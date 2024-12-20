# Generated by Django 5.1.3 on 2024-11-16 15:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appJuegoDeTronos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='characters/')),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('emblem', models.ImageField(blank=True, null=True, upload_to='houses/emblems/')),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(unique=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Departamento',
        ),
        migrations.AddField(
            model_name='character',
            name='house',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='characters', to='appJuegoDeTronos.house'),
        ),
        migrations.AddField(
            model_name='character',
            name='seasons',
            field=models.ManyToManyField(related_name='characters', to='appJuegoDeTronos.season'),
        ),
    ]
