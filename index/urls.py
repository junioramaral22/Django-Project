from django.urls import path

from . import  views

urlpatterns = [
    path('index', views.index),
    path('', views.home),
    path('login', views.login),
    path('register', views.register),
    path('chamados', views.chamados),
]
