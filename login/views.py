from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from navigation.models import purchesinvoice
from django.http import HttpResponse
from .models import *
from .forms import *




def home(request):
    return render(request, 'home.html')

def registration(request):
    form = CreateUserForm()

    if request.method=='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login:login')
    context = {'form': form}
    return render(request, 'registration.html', context)


def second(request):
    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('navigation:about')
    context = {"c":list(purchesinvoice.objects.filter().values('batchno'))}
    return render(request, 'second.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login:login')




