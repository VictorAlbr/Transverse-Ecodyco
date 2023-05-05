
from django.shortcuts import render

import matplotlib.pyplot as plt
import random

population = 100000
air_quality = 80
water_quality = 70
soil_quality = 60
waste_production = 50
food_production = 6000
energy_consumption = 700
budget = 1000000
tax_rate = 0.1
nb_tour = 0

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
    global list_air, list_water, list_nb_tour, list_soil, list_waste
    global list_food, list_energy, list_budget
    # Mettre à jour les paramètres en fonction de l'action passée
    if action == "1":
        air_quality += 5
        soil_quality += 5
        budget -= 5000
        nb_tour+=1

    elif action == "2":
        water_quality += 10
        budget -= 10000
        nb_tour += 1

    elif action == "3":
        waste_production -= 5
        budget -= 5000
        nb_tour += 1

    elif action == "4":
        food_production += 1000
        budget -= 5000
        nb_tour += 1

    elif action == "5":
        energy_consumption -= 100
        budget -= 20000
        nb_tour += 1

    elif action == "6":
        tax_rate += 0.01
        nb_tour += 1


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

    plt.plot(list_nb_tour, list_air, "g-", label="Air")
    plt.plot(list_nb_tour, list_water, "b-", label="Water")
    plt.plot(list_nb_tour, list_soil, "r-", label="Soil")
    plt.plot(list_nb_tour, list_waste, "k-", label="Waste")
    #plt.plot(list_nb_tour, list_energy, "-", label="Energy")
    #plt.plot(list_nb_tour, list_budget, "-", label="Budget")
    #plt.plot(list_nb_tour, list_food, "-", label="Food")
    plt.legend()
    plt.show()

    context = {
        'population': population,
        'air_quality': air_quality,
        'water_quality': water_quality,
        'soil_quality': soil_quality,
        'waste_production': waste_production,
        'food_production': food_production,
        'energy_consumption': energy_consumption,
        'budget': budget,
    }

    return render(request, 'jeu/game.html', context)