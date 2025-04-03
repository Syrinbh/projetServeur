from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from .forms import RegisterForm
from django.contrib.auth import authenticate,login

def Register_view(request):
    if request.method == 'POST' :
        form = RegisterForm(request.POST)
        if (form.is_valid()):
            user =form.save()
            login(request,user)
            return redirect('Login')
    else : 
        form = RegisterForm()

    return render(request, "tasks/register.html",{'form': form})



def Login_view(request):
    username = ''
    password = ''

    
    if request.method == 'POST' :
        username = request.POST["username"]
        password = request.POST["password"]

        user =authenticate(request, username , password)
        if(user != None):
            login(request,user)
            return redirect('Login')
        
        else :
            print("error : Login-view request ")

    return render(request , "tasks/login.html",{'username' : username,'password' : password})
            

