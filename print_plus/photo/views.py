from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, Http404, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
import re
from .models import *
from .forms import *


@csrf_exempt
def index(request):
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


@login_required
@csrf_exempt
def bucket(request):
    orders = Orders.objects.filter(customer=request.user.username)
    context = {
        'orders': orders,
    }
    return render(request, 'photo/bucket.html', context=context)


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


@csrf_exempt
def ajax_doctype(request):
    data = request.POST
    if data['color'] == 'colored':
        res = {
            'content': 'mimo'
        }
    else:
        types = Documents.objects.filter(type='Черно белая')
        type_list = []
        for i in types:
            type_list.append(i.document)
        res = {
            'content': list(set(type_list))
        }
    return JsonResponse(res)


@csrf_exempt
def ajax_order(request):
    data = request.POST
    try:
        pages = int(data['pages'])
        ex = int(data['ex'])
        color = 'Черно белая' if data['color'] == 'black' else 'Цветная'
        doc_type = 'С картинками' if data['doc_type'] == 'С_картинками' else data['doc_type']
        orders = Documents.objects.filter(type=color, format=data['format'], document=doc_type)
        for i in orders:
            price = int(i.price)
        total_price = price * pages * ex
        res = {
            'error': 'success',
            'price': total_price
        }
        return JsonResponse(res)
    except:
        res = {
            'error': 'Поля "Количество страниц" и "Количество экземпляров" должны быть числовыми'
        }
        return JsonResponse(res)


"""
<QueryDict: {'pages': ['21'], 'ex': ['12'], 'format': ['А4'], 'color': ['colored'], 'doc_type': ['undefined'], 'price': ['Итоговая стоимость:10080р']}>
"""


@csrf_exempt
def ajax_uploadFile(request):
    file_data = request.FILES
    if len(file_data) == 0:
        return HttpResponse('Необходимо выбрать файл для загрузки')
    data = request.POST
    price = re.findall(r'\d+', data['price'])[0]
    color = 'Черно белая' if data['color'] == 'black' else 'Цветная'
    doc_type = '' if data['doc_type'] == 'undefined' else data['doc_type']
    b = Orders(customer=request.user.username, paper_type=color, format=data['format'], document_type=doc_type,
               instance_count=data['ex'], page_count=data['pages'], price=price, file=file_data['file'])
    b.save()
    res = 'success'
    return HttpResponse(res)


@csrf_exempt
def ajax_uploadOrder(request):
    file_data = request.FILES
    if len(file_data) == 0:
        return HttpResponse('Необходимо выбрать файл для загрузки')
    data = request.POST
    price = re.findall(r'\d+', data['price'])[0]
    color = 'Черно белая' if data['color'] == 'black' else 'Цветная'
    doc_type = '' if data['doc_type'] == 'undefined' else data['doc_type']
    b = Orders(id=data['id'], customer=request.user.username, paper_type=color, format=data['format'],
               document_type=doc_type,
               instance_count=data['ex'], page_count=data['pages'], price=price, file=file_data['file'])
    b.save()
    res = 'success'
    return HttpResponse(res)
