from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('group/', views.creature_list),
    path('group/<slug:creature>/', views.group_posts),
]