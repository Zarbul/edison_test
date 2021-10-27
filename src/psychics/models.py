import random

from django.db import models


# Create your models here.
class Psychics(models.Model):
    name = models.CharField(max_length=50, default='psychics', unique=True)
    all_numders = models.CharField(max_length=300, null=True, blank=True, default='')
    credibility = models.IntegerField(default=0, blank=True, null=True)

    def psy_num(self):
        return random.randint(10, 99)


    def __str__(self):
        return self.name
