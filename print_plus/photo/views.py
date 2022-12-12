from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, Http404, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt

from .models import *
from .forms import *

@csrf_exempt
def index(request):
    # if 'registration' in request.POST:
    #     print(1112131313)
    #     register_form = RegisterUserForm(request.POST)
    #     if register_form.is_valid():
    #         register_form.save()
    #         messages.success(request, 'Account created successfully')
    #         return redirect('home')
    # else:
    register_form = RegisterUserForm()
    color_docs = Documents.objects.filter(type='Цветная')
    black_docs = Documents.objects.filter(type='Черно белая')
    login_form = LoginUserForm()
    context = {
        'color_docs': color_docs,
        'black_docs': black_docs,
        'login_form': login_form,
        'register_form': register_form,
    }
    return render(request, 'photo/index.html', context=context)


def logout_user(request):
    logout(request)
    return redirect('home')


@csrf_exempt
def ajax_login(request):
    data = request.POST
    username = data['nick']
    password = data['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            res = {
                'error': 'success'
            }
            return JsonResponse(res)
    else:
        res = {
            'error': 'Неправильно указан логин и/или пароль',
        }
        return JsonResponse(res)


@csrf_exempt
def ajax_registr(request):
    data = request.POST
    username = data['username'].lower()
    new = User.objects.filter(username=username)
    if new.count():
        res = {
            'error': 'Пользователь уже существует',
        }
        return JsonResponse(res)
    if data['password1'] != data['password2']:
        res = {
            'error': 'Пароли не совпадают',
        }
        return JsonResponse(res)
    else:
        user = User.objects.create_user(
            data['username'],
            '',
            data['password1'],
        )
        if user is not None:
            if user.is_active:
                login(request, user)
        res = {
            'error': 'success'
        }
        return JsonResponse(res)

