# Generated by Django 5.1.3 on 2024-12-06 17:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appJuegoDeTronos', '0008_character_seasons_alter_character_house_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='image',
        ),
        migrations.AddField(
            model_name='character',
            name='is_alive',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='house',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='characters', to='appJuegoDeTronos.house'),
        ),
        migrations.AlterField(
            model_name='character',
            name='seasons',
            field=models.ManyToManyField(related_name='characters', to='appJuegoDeTronos.season'),
        ),
    ]