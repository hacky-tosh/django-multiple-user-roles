from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

from django.contrib import  messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .decorators import *
from django.contrib.auth.models import Group


# Create your views here.
@unauthenticated_user
def loginuser(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.info(request,f'username or password is incorrect')
            return render(request, 'login.html')




    return render(request,'login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')



@unauthenticated_user
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='organizer')
            user.groups.add(group)

            messages.success(request,f"Account created for {username}")
            return redirect('login')


    context={'form':form}
    return render(request,'register.html',context)

@login_required(login_url='login')
@admin_only
def dashboard(request):
    return render(request,'dashboard.html')\

@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def lowdashboard(request):
    return render(request,'dashboard2.html')