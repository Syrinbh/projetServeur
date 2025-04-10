from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.


class Task(models.Model): 
    title = models.CharField(max_length=200,default='none')
    statut = models.CharField(max_length=200,default='none')
    description = models.TextField()
    #description = models.CharField(max_length=200)
    parentTask = models.CharField(max_length=200,default='none')
    sonTask = models.CharField(max_length=200,default='none')
        
class User(AbstractUser):
    #name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    

class Team(models.Model):
    name = models.CharField(max_length=200)



class CreatTask ():
    Parent = models.ForeignKey('self',on_delete=models.SET_NULL)
    createdby = models.ForeignKey('User',on_delete=models.SET_NULL)
    assignedUsers = models.ManyToManyField('User')
    assignedTeams = models.ManyToManyField('Team')