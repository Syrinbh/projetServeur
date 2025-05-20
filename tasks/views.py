from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.
from django.http import HttpResponse
#from .forms import RegisterForm
from .forms import * 
from .models import Task
#from .forms import Taskform
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from . import views
from .models import Team
from django.http import HttpResponseForbidden


def Register_view(request):
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
    if request.method == 'POST' :
        username = request.POST["username"]
        password = request.POST["password"]

        #user =authenticate(request, username , password)
        user = authenticate(request, username=username, password=password)

        if user:
            login(request,user)
            return redirect('home')
        
    return render(request , "tasks/login.html")
            
def Logout_view(request):
    logout(request)
    return redirect('home')


def home(request):
    return render(request, "tasks/home.html")

@login_required
def Create_task_view(request):
    if request.method == 'POST':
        form = Taskform(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.createdby = request.user
            task.save() 
            form.save_m2m() 
            return redirect('home')
            

    else:
        form = Taskform()
    return render(request,'tasks/Create_task.html',{'form': form})

def List_task_view(request): 
    tasks = Task.objects.all()
    return render(request, 'tasks/List_task.html', {'tasks': tasks})



#doit prendre createdby dans getobjector404
@login_required
def delete_task_view(request,task_id):
    task = get_object_or_404(Task,id=task_id,createdby=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('list')
    return render(request,'tasks/Delete_task.html', {'task':task})

@login_required
def update_task_view(request, task_id):
    task = get_object_or_404(Task, id=task_id )
    if request.user != task.createdby or request.user not in task.assignedUsers :
        return HttpResponseForbidden("Vous n'avez pas le droit de modifier la tâche ")
    if request.method == 'POST':
        form = Taskform(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('list')  
    else:
        form = Taskform(instance=task)
    return render(request, 'Update_task.html', {'form': form})

#Team 
def List_team_view(request):
    teams =Team.objects.all()
    return render(request,'tasks/List_teams.html',{'teams' : teams})
    teams =Team.objects.all()
    return render(request,'tasks/List_team.html',{'team' : form})

@login_required
def create_team_view(request):
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
    team = get_object_or_404(Team, id=team_id)
    
    if request.method == 'POST':
        # Ajouter l'utilisateur à l'équipe
        team.members.add(request.user)
        return redirect('joinTeam')
    
    # Vérifier si l'utilisateur est déjà membre
    
    is_member = team.members.filter(id=request.user.id).exists()
    
    
    return render(request, 'tasks/Join_team.html', {
        'team': team,
        'is_member': is_member
    })

@login_required
def quit_team_view(request,team_id):
    team = get_object_or_404(Team, id=team_id)

    if request.method == 'POST':
        team.members.remove(request.user)
        return redirect('home')

    return render(request, 'tasks/quit_team.html', {'team': team})

@login_required
def delete_team_view(request, team_id):
    team = get_object_or_404(Team,id = team_id)
    if request == 'POST':
        team.delete()
        return redirect('home')
    
    return render(request,'tasks/Delete_team.html', name = 'deleteTeam')
'''

@login_required
def update_task_view(request, task_id):
    task = get_object_or_404(Task, id=task_id )
    return redirect('home')
@login_required
def update_task_view(request, task_id):
    if request.method == 'POST':
        return redirect('home')
'''
