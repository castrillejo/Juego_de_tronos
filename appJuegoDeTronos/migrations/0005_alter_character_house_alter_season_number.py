# Generated by Django 5.1.3 on 2024-11-17 18:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appJuegoDeTronos', '0004_alter_character_house_alter_character_seasons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='house',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='characters', to='appJuegoDeTronos.house'),
        ),
        migrations.AlterField(
            model_name='season',
            name='number',
            field=models.IntegerField(),
        ),
    ]
