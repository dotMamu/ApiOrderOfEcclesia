from django.db import models

# Create your models here.

class GlyphUnion(models.Model):
    name = models.CharField(max_length=200)
    alias = models.CharField(max_length=200)
    attack = models.CharField(max_length=200, blank=True, null=True)
    attribute = models.CharField(max_length=200, blank=True, null=True)
    consume = models.CharField(max_length=200)
    effect = models.CharField(max_length=200)
    notes = models.CharField(max_length=200, blank=True, null=True)
    slot1 = models.CharField(max_length=200, blank=True, null=True)
    slot2= models.CharField(max_length=200, blank=True, null=True)
    back = models.CharField(max_length=200, blank=True, null=True)



class Weapon(models.Model):
    name = models.CharField(max_length=200)
    alias = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    attributes= models.CharField(max_length=200, null=True, blank=True)
    statistics = models.CharField(max_length=200, null=True, blank=True)
    found = models.CharField(max_length=200)
    consume = models.CharField(max_length=200)
    notes = models.CharField(max_length=200 , blank=True, null=True)
    

