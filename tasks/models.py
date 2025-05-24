from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.

"""_
Contient tous les models d'objets utilisés par le serveur
Ce sont des objets indépendants qui étendent des models de django afin
de pouvoir être appele par le programme principal du serveur
"""
class Task(models.Model): 
    statutChoice = [('privée','Privée'),('publique','Publique')]
    title = models.CharField(max_length=200,default='none')
    statut = models.CharField(max_length=200,choices=statutChoice,default='privée')
    description = models.TextField()
    private = models.BooleanField(default=False)
    Parent = models.ForeignKey('self',null = True,blank=True,on_delete=models.SET_NULL,related_name="subtask")
    createdby = models.ForeignKey('User',null=True,blank=True,on_delete=models.SET_NULL,related_name='createdTasks')
    assignedUsers = models.ManyToManyField('User')
    assignedTeams = models.ManyToManyField('Team',related_name='assigned_tasks',blank=True)
        
class User(AbstractUser):
    #name = models.CharField(max_length=200)
    USERNAME_FIELD='username'
    description = models.CharField(max_length=200)
    


class Team(models.Model):
    name = models.CharField(max_length=200)
    members = models.ManyToManyField('User',related_name="teams")  
    task_list = models.ManyToManyField('Task')  # Liste des tâches

    def __str__(self):
        return self.name



