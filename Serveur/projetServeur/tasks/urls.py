
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
    path('create/', views.Create_task_view, name = 'create'), 
    path('list/', views.List_task_view, name = 'list'), 
    path('update/<int:task_id>/', views.update_task_view, name='update'),
    path('delete/<int:task_id>/', views.delete_task_view, name='delete'),
    
    


]