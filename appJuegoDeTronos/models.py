from django.db import models

class House(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Character(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    house = models.ForeignKey('House', null=True, blank=True, on_delete=models.SET_NULL, related_name='characters')
    seasons = models.ManyToManyField('Season')

    def __str__(self):
        return self.name

class Season(models.Model):
    number = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f"Season {self.number}"
