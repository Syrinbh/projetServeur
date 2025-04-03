
from django.contrib import admin
from django.urls import path
from . import views

#from . import views
 #il y'a espace apres le point , sinon erreur 


urlpatterns = [
    path('register/', views.Register_view, name = 'Register'),
    path('Login/', views.Login_view, name = 'Login'),
    # path('')


]