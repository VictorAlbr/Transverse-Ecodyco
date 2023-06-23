# Transverse-Ecodyco
Ce projet consiste en un simulateur de ville développé en Django, une framework Python populaire pour le développement web.

Dans ce jeu, vous êtes en charge de la gestion d'une ville avec différentes variables telles que la qualité de l'air, la qualité de l'eau, la qualité du sol, la production de déchets, la production de nourriture, la consommation d'énergie, le budget et le taux d'imposition.

Fonctionnalités
Les actions du joueur peuvent affecter ces variables, par exemple, augmenter la qualité de l'air, augmenter la qualité de l'eau, réduire la production de déchets, augmenter la production de nourriture, réduire la consommation d'énergie, etc.
Chaque action a un coût de budget associé.
Le budget est mis à jour en fonction des revenus fiscaux et des coûts de gestion.
Les données sont stockées à chaque tour pour permettre un suivi de l'évolution des variables au fil du temps.
Le programme génère un graphique radar pour visualiser les variables de la ville à chaque tour.
Utilisation
Exécutez le fichier views.py dans un environnement Django et naviguez vers l'URL indiquée pour commencer à jouer. Sélectionnez une action à chaque tour pour tenter d'améliorer votre ville tout en gardant votre budget sous contrôle.

Requis
Python 3.5+
Django 2.0+
numpy
matplotlib
random
Code
La logique principale du jeu se trouve dans la fonction game dans views.py. Cette fonction est appelée à chaque tour du jeu et met à jour les variables de la ville en fonction de l'action choisie par le joueur. L'état actuel du jeu est ensuite renvoyé à l'utilisateur sous forme de réponse HTTP.

Avertissement
Ce projet est toujours en cours de développement. Certaines fonctionnalités peuvent ne pas fonctionner comme prévu. Nous vous recommandons de tester soigneusement toutes les fonctionnalités avant d'utiliser ce code dans un environnement de production.
