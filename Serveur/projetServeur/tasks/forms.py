#page pour formulaire d'utilisateur 

from django.contrib.auth.forms import UserCreationForm 
from .models import User
from django import forms 

class RegisterForm (UserCreationForm ):
    class Meta : 
        model = User 
        fields = ['username', 'email', 'description', 'password1', 'password2' ]
        
class Taskform(forms.ModelForm):
    class Meta :
        model = User
        fields = ['title', 'statut', 'description', 'parentTask', 'sonTask' ]