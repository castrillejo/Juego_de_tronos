from django.db import models
from django.utils.translation import gettext_lazy as _

class House(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("House Name"))
    description = models.TextField(verbose_name=_("House Description"))
    image = models.ImageField(upload_to='', null=True, blank=True)
    def __str__(self):
        return self.name
from django.db import models
class Character(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    description = models.TextField(verbose_name=_("Description"))
    house = models.ForeignKey('House', on_delete=models.SET_NULL, null=True, related_name='characters')
    seasons = models.ManyToManyField('Season', related_name='characters')
    image = models.ImageField(upload_to='characters/', null=True, blank=True)
    is_alive = models.BooleanField(default=True) 

    def __str__(self):
        return self.name



class Season(models.Model):
    number = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f"Season {self.number}"