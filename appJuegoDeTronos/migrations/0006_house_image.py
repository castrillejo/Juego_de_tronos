# Generated by Django 5.1.3 on 2024-11-17 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appJuegoDeTronos', '0005_alter_character_house_alter_season_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
