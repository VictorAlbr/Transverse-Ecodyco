from django.urls import path
from . import views

urlpatterns = [
    path('jeu/', views.game, name='jeu'),
    path('game/action/<str:action>/', views.game, name='game_action'),
]