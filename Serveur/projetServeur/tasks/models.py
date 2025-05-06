from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.


class Task(models.Model): 
    title = models.CharField(max_length=200,default='none')
    statut = models.CharField(max_length=200,default='none')
    description = models.TextField()
    #description = models.CharField(max_length=200)
    private = models.BooleanField(default=False)
    Parent = models.ForeignKey('self',null = True,blank=True,on_delete=models.SET_NULL,related_name="subtask")
    createdby = models.ForeignKey('User',null=True,blank=True,on_delete=models.SET_NULL,related_name='createdTasks')
    assignedUsers = models.ManyToManyField('User')
    assignedTeams = models.ManyToManyField('Team')
        
class User(AbstractUser):
    #name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    

class Team(models.Model):
    name = models.CharField(max_length=200)
    members = models.ManyToManyField('User')  
    task_list = models.ManyToManyField('Task')  # Liste des tâches



