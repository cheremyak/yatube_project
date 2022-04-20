from django.http import HttpResponse
from django.shortcuts import render


def index(request):
     template = 'posts/index.html'
     title = 'Это главная страница проекта Yatube'
     text = 'Последние обновления на сайте'
     context = {
          'title': title,
          'text': text,
     }
     return render(request, template, context)


def group_list(request):
     template = 'posts/group_list.html'
     group_title = 'Группы проекта'
     group_text = 'Здесь будет информация о группах проекта Yatube'
     context = {
          'title': group_title,
          'text': group_text,
     }

     return render(request, template, context)


def group_posts(request, blogger):
    return HttpResponse(f'Данные блогеры относятся к группе {blogger}')
    