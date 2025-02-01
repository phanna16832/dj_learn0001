from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import User_Data

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the home page
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login_form.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/')
@login_required(login_url='/')
def home(request):
    context = {
        'username': request.user.username,  # Directly using the logged-in user's username
    }
    return render(request, 'home.html', context)
