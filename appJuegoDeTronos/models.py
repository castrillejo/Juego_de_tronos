from django.db import models

class House(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Season(models.Model):
    number = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return f"Season {self.number}"

class Character(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    house = models.ForeignKey(House, related_name='characters', on_delete=models.CASCADE)
    seasons = models.ManyToManyField(Season, related_name='characters')

    def __str__(self):
        return self.name
