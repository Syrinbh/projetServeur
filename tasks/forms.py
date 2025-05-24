#page pour formulaire d'utilisateur 

from django.contrib.auth.forms import UserCreationForm 
from .models import User
from .models import Task
from django import forms 
from .models import Team

"""
    Represente tous mes formulaires que peut avoir le site avec lesquels
    les utilisateurs vont pouvoir interragir
"""
class RegisterForm (UserCreationForm ):
    class Meta : 
        model = User
        fields = ['username', 'email', 'description', 'password1', 'password2' ]

        
class Taskform(forms.ModelForm):
    class Meta :
        model = Task
        fields = ['title', 'statut', 'description', 'Parent','assignedUsers','assignedTeams']

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'members']


