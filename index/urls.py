from django.urls import path

from . import  views

urlpatterns = [
    path('index', views.index),
    path('', views.home),
    path('login', views.login),
    path('register', views.register),
    path('chamados', views.chamados),
    path('edit/<int:id>', views.editChamados, name="edit-chamado"),
    path('delete/<int:id>', views.deleteChamados, name="delete-chamado"),
]
