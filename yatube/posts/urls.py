from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('group/', views.group_list),
    path('group/<slug:blogger>/', views.group_posts),
]