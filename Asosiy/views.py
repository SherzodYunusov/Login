from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *


def plan(request):
    if request.method == 'POST':
        Plan.objects.create(foydalanuvchi = request.user,
            sarlavha=request.POST['s'],
            batafsil=request.POST['b'],
            vaqt=request.POST['sana'],
            holat=request.POST['holat'],
        )
        return redirect('/plan/')
    if request.user.is_authenticated:
        content = {
            'reja': Plan.objects.filter(foydalanuvchi = request.user),
        }
        return render(request, 'index.html',content)
    return redirect('/')

def ochirish_plan(request, son):
    Plan.objects.filter(id=son, foydalanuvchi = request.user).delete()

    return redirect('/plan/')


def login1(request):
    if request.method == 'POST':
        user = authenticate(
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        if user is None:
            return redirect("/")
        login(request, user)
        return redirect("/plan/")
    return render(request, 'login.html')

def edit(request):
    return render(request, 'edit.html')


def logout1(request):
    logout(request)
    return redirect('/')


# Create your views here.
