# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 11:19:40 2022


@author: freez
"""

import random as rnd
import matplotlib.pyplot as g
import math as m

# def big_sequence():
#     counter=0
#     while True:
#         yield counter
#         counter+=1


def graph2D_placePoint(x, y, point_line):
    if point_line == "point":
        g.plot(x, y, 'r*')
    elif point_line == "line":
        g.plot(x, y, label="point_line")
    else:
        print("Error plotting")

def Var_contraintes():
    Nb_villes=rnd.randint(0, 10)
    Capacite_vehicule=rnd.randint(0, int(1000+0.1*Nb_villes))
    Temps_transfert=rnd.randint(0, int(1000+0.3*Nb_villes))
    return (Nb_villes, Capacite_vehicule, Temps_transfert)

x = [48.8566,
     43.2964,
     45.76,
     43.6045,
     43.7034,
     47.2181,
     43.6119,
     48.5833,
     44.84,
     50.6278,
     48.1147,
     49.2628,
     43.1258,
     45.4347,
     49.49,
     45.1715,
     45.7667,
     47.3167,
     47.4736,
     43.838,
     45.7831,
     48.0077
     ]
y = [2.3522,
     5.37,
     4.84,
     1.444,
     7.2663,
     - 1.5528,
     3.8772,
     7.7458,
     - 0.58,
     3.0583,
     - 1.6794,
     4.0347,
     5.9306,
     4.3903,
     0.1,
      5.7224,
     4.8803,
     5.0167,
     - 0.5542,
     4.361,
     3.0824,
     0.1984
     ]
graph2D_placePoint(x, y, "point")
norme=[]
liste_NbVilles=[]
liste_tParcours=[]
liste_cap=[]
#rnd.seed(3)
for i in range(len(x)):
    a=111.39*x[i]                   #conversion en metres pour latitude
    b=111.39*m.cos(x[i])*y[i]       #conversion en metres pour longitude
    norme.append(m.sqrt(a**2+b**2)) #calcul de norme d'une ville à une autre
    
    n, Cap_camion, T_n=Var_contraintes()    #Z=((60+10n)/n)*X+((50+10n)n)*Y+n
    print("Contraintes", T_n, Cap_camion, n)
    liste_NbVilles.append(T_n)
    liste_tParcours.append(Cap_camion)
    liste_cap.append(n)
print(norme)
liste_poids=[]
matrice_poids=[]                    #matrice 2x2, regarder plus bas
for i in range(len(liste_NbVilles)):
    liste_poids.append(int(((liste_NbVilles[i]+liste_cap[i]+liste_tParcours[i])/100)))
    
while liste_poids!=[]:
    matrice_poids.append(liste_poids[:1])   #prendre tout jusqu'au 1er élèment de la liste, donc 1 seul élèment
    liste_poids=liste_poids[1:]     #prendre tout jusqu'au 1er élèment de la liste, donc 1 seul élèment
    
print (matrice_poids)
# r* pour afficher des points ; afficher des graphes pour chaque gén. de func. contraintes
# afficher points sur un graphe
g.legend()
