from django.urls import path

from . import views

#yatube/posts/urls.py
app_name = 'posts'

urlpatterns = [
    path('', views.index, name=''),
    path('index.html', views.index, name='index'),
    path('group/<slug:slug>/', views.group_posts, name='group_posts'),
]