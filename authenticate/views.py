from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from authenticate.forms import LoginForm, RegisterForm


def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid:
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user=authenticate(username=username, password=password)
            login(request, user)
            return redirect('schools')
    
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('schools')
        else:
            return redirect('login')

    #     form = LoginForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('schools')
    # form = LoginForm()
    else:
        return render(request, 'login.html')
    # return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return render(request, 'login.html')
