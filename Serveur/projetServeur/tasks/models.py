from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.


class Task(models.Model): 
    title = models.CharField(max_length=200)
    statut = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
        
class User(AbstractUser):
    #name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    

class Team(models.Model):
    name = models.CharField(max_length=200)

        