from django.urls import path

from . import views

#yatube/posts/urls.py
app_name = 'posts'

urlpatterns = [
    path('group/<slug:slug>/', views.group_posts, name='group_posts'),
    path('', views.index, name='index'),  
]