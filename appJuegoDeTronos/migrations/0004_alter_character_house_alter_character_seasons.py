# Generated by Django 5.1.3 on 2024-11-17 18:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appJuegoDeTronos', '0003_remove_character_image_remove_house_emblem_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='house',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='appJuegoDeTronos.house'),
        ),
        migrations.AlterField(
            model_name='character',
            name='seasons',
            field=models.ManyToManyField(to='appJuegoDeTronos.season'),
        ),
    ]
