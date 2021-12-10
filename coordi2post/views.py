from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def signinview(request):
    if request.method == 'GET':
        return render(request, 'sign/signin.html')
    else:
        username_data = request.POST.get('username')
        password_data = request.POST.get('password')
        print(username_data, password_data)
        
        user = authenticate(username=username_data, password=password_data)
        if user:
            login(request, user)
            return redirect('main')
        else:
            return render(request, 'sign/signin.html')

@login_required
def mainview(request):
    return render(request, 'main/main.html')

def logoutview(request):
    logout(request)
    return redirect('signin')

