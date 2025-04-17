#page pour formulaire d'utilisateur 

from django.contrib.auth.forms import UserCreationForm 
from .models import User
from .models import Task
from django import forms 

class RegisterForm (UserCreationForm ):
    class Meta : 
<<<<<<< HEAD
        model = User 
        fields = ['username', 'email', 'description', 'password' ]
=======
        model = User
<<<<<<< HEAD
        fields = ['username', 'email', 'description', 'password1' ]
=======
        fields = ['username', 'email', 'description', 'password1', 'password2' ]
>>>>>>> 35567a784f9ff39d1299bd7863ba658df3f7448c
>>>>>>> eff9dad16b00c5364c7bd64f89ef74a0f0eeeb99
        
class Taskform(forms.ModelForm):
    class Meta :
        model = Task
        fields = ['title', 'statut', 'description', 'Parent', 'createdby' ,'assignedUsers','assignedTeams']


# class Task(forms.ModelForm):
#     class Meta:
