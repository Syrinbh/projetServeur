
from django.contrib import admin
from django.urls import path
from . import views
from tasks import views

"""
urlpatterns contient tout les liens utiliser dans les templates pour naviguer 
sur le site et fait en sorte de rendre opaque l'adresse URI
"""

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.Register_view, name = 'register'),
    path('login/', views.Login_view, name = 'login'),
    path('logout/',views.Logout_view,name='logout'),
    
    path('create/', views.Create_task_view, name = 'create'), 
    path('list/', views.List_task_view, name = 'list'), 
    path('update/<int:task_id>/', views.update_task_view, name='update'),
    path('delete/<int:task_id>/', views.delete_task_view, name='delete'),
    
    path('createTeam/', views.create_team_view, name='createTeam'),
    path('joinTeam/<int:team_id>/', views.join_team_view, name='joinTeam'),
    path('quitTeam/<int:team_id>/', views.quit_team_view, name='quitTeam'),
    path('deleteTeam<int:team_id>/', views.delete_team_view, name='deleteTeam'),
    path('listTeam/',views.List_team_view, name='listTeam'),
    path('team/<int:team_id>/',views.team_profile_view, name='teamProfile'),
    path('member/<int:member_id>/',views.member_profile_view, name='memberProfile')

]