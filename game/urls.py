from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('worldmap', views.worldmap, name='worldmap'),
        path('battle', views.battle, name='battle'),
        path('options', views.options, name='options'),
        path('options/save_game', views.save_game, name='options'),
        path('options/load_game', views.load_game, name='options'),
        path('moviedex', views.moviedex, name='moviedex'),
        path('moviedex/info_movie', views.info_movie, name='info_movie'),
]
