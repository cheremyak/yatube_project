from django.http import HttpResponse
from django.shortcuts import render


def index(request):
     template = 'posts/index.html'
     return render(request, template)


def group_list(request):
     return HttpResponse('Список блогеров.')


def group_posts(request, blogger):
    return HttpResponse(f'Данные блогеры относятся к группе {blogger}')
    