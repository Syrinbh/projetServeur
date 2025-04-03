#page pour formulaire d'utilisateur 

from django.contrib.auth.forms import UserCreationForm 
class RegisterForm (UserCreationForm ):
    class Meta : 
        Model = user 
        fileds = [’username’, ‘email’, ‘description’, ‘password1’, ‘password2’ ]
        