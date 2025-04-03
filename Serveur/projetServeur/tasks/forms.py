#page pour formulaire d'utilisateur 

from django.contrib.auth.forms import UserCreationForm 
from .models import User
class RegisterForm (UserCreationForm ):
    class Meta : 
        Model = User 
        fileds = ['username', 'email', 'description', 'password1', 'password2' ]
        