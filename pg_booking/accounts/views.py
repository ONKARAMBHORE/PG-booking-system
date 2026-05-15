from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
# Create your views here.

def register_user(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Account Created Successfully!")

            return redirect('login')
        
    else:

        form = RegisterForm()


    return render(request, 'register.html', {'form': form})




def login_user(request):

    if request.method == 'POST':

        form = AuthenticationForm(data=request.POST)

        if form.is_valid():

            user = form.get_user()

            login(request, user)
            
            messages.success(request, "Logged in successfully!")

            return redirect('pg_list')
        
    else:

        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})




def logout_user(request):

    logout(request)

    messages.success(request, "Logged out successfully!")

    return redirect('login')