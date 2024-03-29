from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user=authenticate(username=username, password=password)
            login(request, user)
            return redirect('../../schools')
                
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('../../schools')
        else:
            messages.success(request, "Il y a eu une erreur dans vos identifiants de connexion, réessayez.")
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout_view(request):
    logout(request)
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return redirect('../../schools')
