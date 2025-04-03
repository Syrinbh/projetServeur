from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .forms import RegisterForm

def Register_view(request):
    if request.method == 'POST' :
        form = RegisterForm(request.POST)
        if (form.is_valid()):
            user =form.save()
            login(request,user)
            return redirect('login')

    return render(request, "tasks/register.html",{'form': form})



def Login_view(request):
    # if request.method == 'POST' :
        

    return HttpResponse("Page de connexion")