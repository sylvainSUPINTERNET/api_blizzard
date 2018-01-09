from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth import logout


from . import forms

# -- HOME --
def home(request):
    context = {'message': 'Welcom on API Blizzard', 'path_signup': 'signup', 'path_login': 'login', 'path_logout': 'logout  '}
    return render(request, 'home.html', context)

# -- REGISTRATION --
def signup(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = forms.SignUpForm()
    return render(request, 'signup.html', {'form': form})



@login_required
def user_logout(request):
    logout(request)
    return  HttpResponseRedirect('home')


def user_login(request):
    if request.method == 'POST':

        user_name = request.POST['firstname']
        user_password = request.POST['password']

        user = authenticate(request, username=user_name, password=user_password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect('home')
        else:
            return HttpResponseRedirect('login')
    else:
        return render(request, 'login.html', {'action_link': 'login'})


