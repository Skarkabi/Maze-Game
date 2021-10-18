from django.urls import path

from . import views

urlpatterns = [
    path('', views.easyRedirect, name="index"),
    path('easy', views.easy, name='index'),
    path('medium', views.medium, name='index'),
    path('hard', views.hard, name='index'),
]