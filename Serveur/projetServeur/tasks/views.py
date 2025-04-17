from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.
from django.http import HttpResponse
#from .forms import RegisterForm
from .forms import * 
from .models import Task
#from .forms import Taskform
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required


def Register_view(request):
    if request.method == 'POST' :
        form = RegisterForm(request.POST)
        if (form.is_valid()):
            user =form.save()
            login(request,user)
            return redirect('login')
    else : 
        form = RegisterForm()

    return render(request, "tasks/register.html",{'form': form})



def Login_view(request):
    username = ''
    password = ''

    
    if request.method == 'POST' :
        username = request.POST["username"]
        password = request.POST["password"]

        #user =authenticate(request, username , password)
        user = authenticate(request, username=username, password=password)

        if(user != None):
            login(request,user)
            return redirect('login')
        
        else :
            print("error : Login-view request ")

    return render(request , "tasks/login.html",{'username' : username,'password' : password})
            



def home(request):
    return render(request, "tasks/home.html")


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
        return redirect('home')
    return render(request,'tasks/Delete_task.html', {'task':task})

'''
@login_required
def update_task_view(request, task_id):
    task = get_object_or_404(Task, id=task_id )
    return redirect('home') 
'''
'''

@login_required
def update_task_view(request, task_id):
    if request.method == 'POST':
        return redirect('home')
'''