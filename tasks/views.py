

#Imports

from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Q
from django.http import HttpResponse
from .forms import * 
from .models import Task
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from . import views
from .models import Team
from django.http import HttpResponseForbidden






#################################################
#                   Login/Register              #
#################################################


def Register_view(request):
    """
    Vue du register
    Si réussi à s'enregistrer dans la BDD, le connecte en même temps
    (Peut-être pas le meilleur choix niveau sécurité mais permet de savoir si
    on est bien enregistré facilement et évite des étapes intermédiaires peu utiles)
    Args:
        request: Requete envoyée au serveur
    Returns:
        function: Une fonction qui redirige sur la page Home si le formulaire est valide,
        sinon fait le rendue de la page Register
    """
    if request.method == 'POST' :
        form = RegisterForm(request.POST)
        if (form.is_valid()):
            user =form.save()
            login(request,user)
            return redirect('home')
    else : 
        form = RegisterForm()

    return render(request, "tasks/register.html",{'form': form})


def Login_view(request):
    """
    Vue du Login
    Prend le Username et le password. (Par défaut dans django)
    Args:
        request: Requete envoyé au serveur
    Returns:
        function: fonciton qui redirige sur la page home si Logged, 
        sinon fait le rendue de la page Login
    """

    if request.method == 'POST' :
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user:
            login(request,user)
            return redirect('home')
        
    return render(request , "tasks/login.html")


def Logout_view(request):
    """
    Vue du logout 
    Args:
        request: Requete envoyé au serveur
    Returns:
        function : fonction qui redirige sur la page principale après avoir déconnecté  
    """

    logout(request) #appel la fonction logout de django
    return redirect('home')


#################################################
#                   Home                        #
#################################################
def home(request):
    """
    Vue de la page principale

    Args: 
        request: Requete envoyé au serveur
    Returns:
        function: fait le rendue de la page d'accueil
    """
    return render(request, "tasks/home.html")



#################################################
#                   Tasks                       #
#################################################


@login_required
def Create_task_view(request):
    """
    Vue pour créer une tache
    /!\ Nécessite d'être connecté
    Enregistre la tâche dans la base de donnée ainsi que le formulaire
    saisie si le formulaire est valide
    Remplie automatiquement 'createdBy' par l'utilisateur qui envoie la requête
     
    Args:
        request: Une requete envoyé au serveur

    Returns :      
        function: Redirige sur la page d'accueil si tout est ok, sinon fait le rendue 
        sur la page actuelle
    
    """ 
    if request.method == 'POST':
        form = Taskform(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.createdby = request.user
            task.save()     #sauvegarde de la tache
            form.save_m2m() #sauvegarde du many to many
            return redirect('home')
            

    else:
        form = Taskform() #appele le constructeur dans form.py qui prend lui meme le model de Task
    return render(request,'tasks/Create_task.html',{'form': form})


@login_required
def List_task_view(request): 
    """
    Vue de la liste des taches
    /!\ Nécessite d'être connecté
    N'affiche que les pages concernant la personne ou 
    les taches publiques

    Args: 
        request: une requête envoyée au serveur

    Returns:
        function: fait le rendue de la page liste des Tâches
    """
    user = request.user
    public_tasks = Task.objects.filter(statut='publique')
    private_tasks = Task.objects.filter(statut='privée').filter(Q(createdby=user)|Q(assignedUsers=user)|Q(assignedTeams__members=user)).distinct()
    tasks = public_tasks.union(private_tasks)
    return render(request, 'tasks/List_task.html', {'tasks': tasks})



@login_required
def delete_task_view(request,task_id):

    """
    Vue pour supprimer une tâche
    /!\ Nécessite d'être connecté

    Args :
        request: Requête soumise au serveur
        task_id: Identifiant permettant de savoir quelle tache supprimer
    
    Returns:
        function: redirige sur la liste des tâches si supprimer, 
        sinon fait le rendue de la page de suppression
    """

    task = get_object_or_404(Task,id=task_id,createdby=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('list')
    return render(request,'tasks/Delete_task.html', {'task':task})

@login_required
def update_task_view(request, task_id):
    """
    Vue pour modifier une tâche
    /!\ Nécessite d'être connecté

    Args: 
        request : Requête soumise au serveur
        task_id : Identifiant de la tâche à modifier

    Returns:
        function: Redirige sur la page de list de tâche si ok, 
        sinon fait le rendue de la page avec le formulaire pré-rempli
        pour garder les saisies précédentes
    
    """
    task = get_object_or_404(Task, id=task_id )
    if request.user != task.createdby and request.user not in task.assignedUsers :
        return HttpResponseForbidden("Vous n'avez pas le droit de modifier la tâche ")
    if request.method == 'POST':
        form = Taskform(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('list')  
    else:
        form = Taskform(instance=task)
    return render(request, 'tasks/Update_task.html', {'form': form})


#################################################
#                   Team                        #
#################################################
 
def List_team_view(request):
    """
    Vue de la liste des équipes

    Args:
        request : requête envoyée au serveur

    Returns:
        function: fait le rendue de la page des listes d'équipes
    """
    teams =Team.objects.all()
    return render(request,'tasks/List_team.html',{'teams' : teams})

@login_required
def create_team_view(request):
    """
    Vue pour créer une équipe
    /!\ Nécessite d'être connecté

    Args:
        request : la requête soumise au serveur

    Returns:
        function: redirige sur la page d'accueil si OK, sinon fait le rendu de la
        page pour créer une équipe
    """
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            team = form.save(commit=False)
            team.save()
            form.save_m2m()  # Pour sauvegarder les relations ManyToMany
            return redirect('home')  # Rediriger vers la liste des tâches
    else:
        form = TeamForm(initial={'members': [request.user]})   

    return render(request, 'tasks/Create_team.html', {'form': form})

@login_required
def join_team_view(request, team_id):
    """
    Vue pour rejoindre une équipe
    /!\ Nécessite d'être connecté

    Args:
        request : Requête soumise au serveur
        team_id : Identifiant de la team à rejoindre

    Returns:
        function: redirige sur la page de la liste d'équipe si ok, sinon fait le rendu
        de la page pour joindre une team
    """
    team = get_object_or_404(Team, id=team_id)
    
    if request.method == 'POST':
        # Ajoute l'utilisateur à l'équipe
        team.members.add(request.user)
        return redirect('listTeam')
    
    # Vérifie si l'utilisateur est déjà membre
    
    is_member = team.members.filter(id=request.user.id).exists()
    
    
    return render(request, 'tasks/Join_team.html', {
        'team': team,
        'is_member': is_member
    })

@login_required
def quit_team_view(request,team_id):
    """
    Vue pour quitter une équipe
    /!\ Nécessite d'être connecté


    Args:
        request : Requête soumise au serveur
        team_id : Identifiant de la team à quitter

    Returns:
        function: redirige sur la page de liste des équipes si ok
    """
    team = get_object_or_404(Team, id=team_id)

    if request.method == 'POST':
        team.members.remove(request.user)
        return redirect('listTeam')

    return render(request, 'tasks/Quit_team.html', {'team': team})

@login_required
def delete_team_view(request, team_id):
    """
    Vue pour supprimer une équipe
    /!\ Nécessite d'être connecté


    Args:
        request : Requête soumise au serveur
        team_id : Identifiant de la team à supprimer

    Returns:
        function: redirige sur la page de liste des équipes si ok
    """
    team = get_object_or_404(Team,id = team_id)
    if request.method == 'POST':
        team.delete()
        return redirect('listTeam')
    
    return render(request,'tasks/Delete_team.html', {'team': team})




#################################################
#                   Profiles                    #
#################################################

@login_required
def team_profile_view(request, team_id):
    """

    Vue pour afficher le profil d'une équipe
    /!\ Nécessite d'être connecté


    Args:
        request : Requête soumise au serveur
        team_id : Identifiant de la team à afficher le profile

    Returns:
        function: fait le rendue de la page pour afficher le profile de l'équipe
        passée en paramètre
    """
    team = get_object_or_404(Team, id=team_id)
    tasks = team.assigned_tasks.all()  
    members = team.members.all()
    return render(request, 'tasks/team_profile.html', {'team': team, 'tasks': tasks, 'members': members})

@login_required
def member_profile_view(request, member_id):
    """

    Vue pour afficher le profil d'un membre d'une équipe
    /!\ Nécessite d'être connecté


    Args:
        request : Requête soumise au serveur
        member_id : Identifiant du membre à afficher le profile

    Returns:
        function: fait le rendue de la page pour afficher le profile de du membre
        passée en paramètre
    """
    member = get_object_or_404(User,id= member_id)
    return render(request, 'tasks/member_profile.html', {'member':member})