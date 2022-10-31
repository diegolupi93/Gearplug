from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    

class Productor(models.Model):
    name = models.CharField(max_length=100)

class Planet(models.Model):
    name = models.CharField(max_length=100)
    galaxy = models.CharField(max_length=100)
      

class Movie(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    director = models.CharField(max_length=100)
    productors = models.ManyToManyField(Productor)
    characters = models.ManyToManyField(Character, related_name='movies')
    planets = models.ManyToManyField(Planet)
    
    def __str__(self):
        return self.name