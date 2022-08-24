from django.db import models

# Create your models here.
class Weapon(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    type = models.CharField(max_length=200) 
    attribute = models.CharField(max_length=200) 
    statistic=models.CharField(max_length=200)
    found = models.CharField(max_length=200)
    notes = models.CharField(max_length=200)
    consume= models.CharField(max_length=200)
    notes = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class GUnion(models.Model):
    name = models.CharField(max_length=200)
    attk = models.CharField(max_length=200)
    attribute = models.CharField(max_length=200)
    consume = models.CharField(max_length=200)
    effect = models.CharField(max_length=200)
    notes = models.CharField(max_length=200)
    comb_1 = models.CharField(max_length=200)
    comb_2 = models.CharField(max_length=200)

    def __str__(self):
        return self.name