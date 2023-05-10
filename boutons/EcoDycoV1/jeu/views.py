
from django.shortcuts import render
import numpy as np
import matplotlib.pyplot as plt
from django.views import View
import random
from math import pi
import numpy as np

population = 100000
air_quality = 80
water_quality = 70
soil_quality = 60
waste_production = 50
food_production = 6000
energy_consumption = 700
budget = 1000
tax_rate = 10
nb_tour = 0
energy_electric=70
energy_fossile=50
reserve_nourriture=60
pouvoir_achat_population=50
population_maximale=50
reserve_de_bois=50
R_bois=1                  #qualité des machines qui coupent du bois
reserve_miniere=60
proprete=80
sea_quality=80

list_air = []
list_water = []
list_nb_tour = []
list_soil = []
list_waste = []
list_food = []
list_energy = []
list_budget = []

def stock_data(air, water, soil, waste, food, energy, budget, nb_tour):
    global list_air, list_water, list_nb_tour, list_soil, list_waste
    global list_food, list_energy, list_budget
    list_air.append(air)
    list_water.append(water)

    list_soil.append(soil)
    list_waste.append(waste)
    list_food.append(food)
    list_energy.append(energy)
    list_budget.append(budget)

    list_nb_tour.append(nb_tour)


def game(request, action=None):
    # Paramètres initiaux
    global population, air_quality, water_quality, soil_quality
    global waste_production, food_production, energy_consumption, budget, tax_rate
    global nb_tour
    global list_air
    global energy_electric
    global energy_fossile
    global reserve_nourriture
    global pouvoir_achat_population
    global population_maximale
    global reserve_de_bois
    global reserve_miniere
    global proprete
    global sea_quality
    # Mettre à jour les paramètres en fonction de l'action passée
    if action == "1":
        air_quality += 5
        soil_quality += 5
        budget -= 5000
        nb_tour += 1


    elif action == "2":
        water_quality += 10
        budget -= 10000
        nb_tour += 1

    # ameliorer usine de traitement d'eau
    elif action == "2.5":

        n_traitement_eau += 10
        budget -= 5000

    elif action == "3":
        waste_production -= 5
        budget -= 5000
        nb_tour += 1

    elif action == "3.5":
        n_recyclage += 5
        budget -= 5000

    elif action == "4":
        food_production += 1000
        budget -= 5000
        nb_tour += 1

    elif action == "4.5":
        energy_consumption -= 100
        budget -= 20000

    elif action == "5":
        energy_consumption -= 100
        budget -= 20000
        nb_tour += 1
    elif action == "5.5":
        energy_consumption -= 100
        budget -= 20000

    elif action == "6":
        tax_rate += 0.01
        nb_tour += 1

    # couper du bois = scierie
    elif action == "8":
        """choisir intensité a couper (nb de troncs a couper par tour) entre 0 et 10
        """

        air_quality -= 5 #+ on coupe de troncs plus la qualité change
        #reserve_de_bois += alpha*I-RI² #reserve de bois optenu a la fin

    # pecher
    elif action == "9":
        sea_quality -= 500
        food_production += 1000
        budget -= 5000

    # construire des eoliennes sur terre
    elif action == "10":

        soil_quality -= 10
        energy_electric += 10
        budget -= 5000

    # construire des eoliennes sur mer
    elif action == "19":

        soil_quality -= 10
        energy_electric += 10
        budget -= 5000

    # ameliorer des eoliennes
    elif action == "10.5":
        budget -= 5000

    # construire des barrages/turbine hydro elec
    elif action == "11":
        energy_electric += 1000
        water_quality -= 10
        budget -= 5000

    # ameliorer barrage
    elif action == "11.5":

        budget += 5000

    # construire des habitations
    elif action == "12":
        population_maximale += 1000
        budget += 5000

    # miner
    elif action == "13":
        reserve_miniere += 1000
        soil_quality -= 100
        budget += 5000

    # construire route
    elif action == "14":
        budget += 5000

    # maintenir route
    elif action == "14.5":
        budget -= 5000

    # augmenter reserve nourriture
    elif action == "15":
        reserve_nourriture += 1000
        budget -= 5000

    # exporter nourriture
    elif action == "16":
        reserve_nourriture -= 1000
        budget += 5000

    # exporter energie
    elif action == "17":
        energy_fossile -= 5000
        budget += 5000

    # exporter dechet
    elif action == "18":
        waste_production -= 1000
        budget -= 5000
        soil_quality += 10


    # Mettre à jour les paramètres aléatoirement pour ajouter de la variété
    """air_quality -= random.randint(0, 2)
    water_quality -= random.randint(0, 2)
    soil_quality -= random.randint(0, 2)
    waste_production += random.randint(0, 2)
    energy_consumption += random.randint(0, 10)
    food_production -= random.randint(0, 500)"""

    # Mettre à jour le budget en fonction des revenus fiscaux et des coûts de gestion
    income = population * tax_rate
    expenses = waste_production * 100 + energy_consumption * 0.1 + food_production * 0.5
    budget += income - expenses

    stock_data(air_quality, water_quality, soil_quality, waste_production, food_production, energy_consumption, budget, nb_tour, )

    """plt.plot(list_nb_tour, list_air, "g-", label="Air")
    plt.plot(list_nb_tour, list_water, "b-", label="Water")
    plt.plot(list_nb_tour, list_soil, "r-", label="Soil")
    plt.plot(list_nb_tour, list_waste, "k-", label="Waste")
    #plt.plot(list_nb_tour, list_energy, "-", label="Energy")
    #plt.plot(list_nb_tour, list_budget, "-", label="Budget")
    #plt.plot(list_nb_tour, list_food, "-", label="Food")
    plt.title("ResultatJeu")
    #plt.legend()
    filename= 'static\images\ResultatJeu.png'
    plt.savefig(filename)"""

    def create_radar_chart():
        plt.clf()
        # Number of variables
        num_vars = 17

        # Compute the angle of each axis in the plot
        angles = [n / float(num_vars) * 2 * pi for n in range(num_vars)]
        angles += angles[:1]

        # Initialize the radar chart
        ax = plt.subplot(111, polar=True)

        # Set the first axis on top
        ax.set_theta_offset(pi / 2)
        ax.set_theta_direction(-1)

        # Draw the perimeter and fill the interior with a grid
        plt.xticks(angles[:-1], ['Air', 'Water', 'Soil', 'Waste', 'Food', 'Energy', 'Budget','tax_rate','energy_electric','energy_fossile',
                                 'reserve_nourriture','pouvoir_achat_population','population_maximale','reserve_de_bois','reserve_miniere',
                                 'proprete','sea_quality'], color='grey', size=7)
        ax.set_rlabel_position(0)
        plt.yticks([25, 50, 75], ["25", "50", "75"], color="grey", size=7)
        plt.ylim(0, 100)

        # Add data (use only the last index of each list)
        last_index = len(list_nb_tour) - 1
        values = [air_quality, water_quality, soil_quality,
                  waste_production, food_production / 100,
                  energy_consumption / 10, budget / 10000, tax_rate, energy_electric, energy_fossile,
                  reserve_nourriture, pouvoir_achat_population, population_maximale, reserve_de_bois,
                  reserve_miniere, proprete, sea_quality]
        values += values[:1]
        ax.plot(angles, values, linewidth=1, linestyle='solid')
        ax.fill(angles, values, 'b', alpha=0.1)

        # Add static legend
        plt.figlegend(['Latest values'], loc='upper right', bbox_to_anchor=(0.1, 0.1))

        # Show the radar chart
        plt.title("ResultatJeu")
        # plt.legend()
        filename = 'static\images\ResultatJeu.png'
        plt.savefig(filename)

    context = {
        'population': population,
        'air_quality': air_quality,
        'water_quality': water_quality,
        'soil_quality': soil_quality,
        'waste_production': waste_production,
        'food_production': food_production,
        'energy_consumption': energy_consumption,
        'budget': budget,
        'tax_rate': tax_rate,
        'energy_electric': energy_electric,
        'energy_fossile': energy_fossile,
        'reserve_nourriture': reserve_nourriture,
        'pouvoir_achat_population': pouvoir_achat_population,
        'population_maximale': population_maximale,
        'reserve_de_bois': reserve_de_bois,
        'reserve_miniere': reserve_miniere,
        'proprete': proprete,
        'sea_quality':sea_quality
    }

    def view(request):
        numbers = list(range(101))
        return render(request, 'jeu/game.html', {'numbers': numbers})

    create_radar_chart()
    return render(request, 'jeu/game.html', context)