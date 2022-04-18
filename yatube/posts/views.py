from django.http import HttpResponse


def index(request):
     return HttpResponse('Главная страница проекта Yatube')


def creature_list(request):
     return HttpResponse('Список чудовищ.')


def group_posts(request, creature):
    return HttpResponse(f'Данные чудовища относятся к группе {creature}')
    