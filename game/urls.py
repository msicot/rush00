from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('worldmap', views.worldmap, name='worldmap'),
        path('battle', views.battle, name='battle')
        ]
