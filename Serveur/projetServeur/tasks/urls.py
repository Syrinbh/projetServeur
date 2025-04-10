
from django.contrib import admin
from django.urls import path
from . import views
from tasks import views

#from . import views
 #il y'a espace apres le point , sinon erreur 


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.Register_view, name = 'register'),
    path('login/', views.Login_view, name = 'login'),
    # path('')


]