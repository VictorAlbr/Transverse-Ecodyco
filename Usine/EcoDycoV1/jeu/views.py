from django.shortcuts import render
import numpy as np
import matplotlib.pyplot as plt
from django.views import View
from django.http import JsonResponse
import random
from math import pi

forest_quantity = 500
wood_quantity = 0
flux_max_foret = 10
usure_r = 0.01
temps_usure_bois = 0

#tangente pour simuler l'usure et augmenter R
def tanh_function(x):
    a = 10  # constante de décalage de la fonction vers la droite
    k = 0.5  # constante d'étirement de la fonction selon l'axe x
    y = 1 + np.tanh(k * (x - a))
    return y

def pow3_function(x):
    y = x ** 3
    return y

def game(request, action=None):
    # Paramètres initiaux
    global flux_max_foret
    global forest_quantity
    global wood_quantity
    global flux_max_foret
    global usure_r
    global temps_usure_bois

    if request.method == "POST":
        woodcutting_number = request.POST.get("woodcutting_number", 0)
        print("le nombre de bois est : " + woodcutting_number)

        # Mettez à jour les valeurs de forest_quantity et wood_quantity en fonction de woodcutting_number
        # Par exemple (changez cela en fonction de votre logique de jeu) :
        forest_quantity -= (int(woodcutting_number)*flux_max_foret)/100   #
        i = (int(woodcutting_number)*20)/100# on prend comme valeur i allant de 0 à 20

        alpha = flux_max_foret
        if alpha*i - usure_r*i*i > 0:
            wood_quantity += alpha * i - usure_r * i * i  # on retrouve notre formule du flux tel que phi = alpha*i-Ri²

        temps_usure_bois = temps_usure_bois + pow3_function(int(woodcutting_number)/100)#on augmente notre R en fonction de l'intensité d'usage
        usure_r = 0.01 + tanh_function(temps_usure_bois) #on augmente notre R en fonction de du temps d'usage

        return JsonResponse({
            'forest_quantity': forest_quantity,
            'wood_quantity': wood_quantity,
            'temps_usure_bois': temps_usure_bois,
            'usure_r': usure_r,
        })
    # Mettre à jour les paramètres en fonction de l'action passée
    if action == "1":
        forest_quantity += 10
    # couper du bois = scierie
    elif action == "2":
        temps_usure_bois = 0
        usure_r = 0.01

    context = {
        'forest_quantity': forest_quantity,
        'wood_quantity': wood_quantity,
        'temps_usure_bois': temps_usure_bois,
        'usure_r': usure_r,
    }

    def view(request):
        numbers = list(range(101))
        return render(request, 'jeu/game.html', {'numbers': numbers})

    return render(request, 'jeu/game.html', context)