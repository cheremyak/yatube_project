from django.urls import path

from . import views

#yatube/posts/urls.py
app_name = 'posts'

urlpatterns = [
    path('', views.index, name=''),
    path('index.html', views.index, name='index'),
    path('group_list.html/index.html', views.index, name='group_list_index'),
    path('group_list.html/group_list.html', views.group_list, name='group_group'),
    path('group_list.html/', views.group_list, name='group_list'),
    path('group/<slug:slug>/', views.group_posts, name='group_posts'),
]