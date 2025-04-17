#page pour formulaire d'utilisateur 

from django.contrib.auth.forms import UserCreationForm 
from .models import User
from .models import Task
from django import forms 

class RegisterForm (UserCreationForm ):
    class Meta : 
        model = User
        fields = ['username', 'email', 'description', 'password1' ]
        
class Taskform(forms.ModelForm):
    class Meta :
        model = Task
        fields = ['title', 'statut', 'description', 'Parent', 'createdby' ,'assignedUsers','assignedTeams']


# class Task(forms.ModelForm):
#     class Meta:
