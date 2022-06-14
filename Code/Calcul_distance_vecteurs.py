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


def graphe2D_placePoint(x, y, point_line):
    if point_line == "point":
        g.plot(x, y, 'r*')
    elif point_line == "line":
        g.plot(x, y, label="point_line")
    else:
        print("Error plotting")


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
graphe2D_placePoint(x, y, "point")
norme=0
for i in range(len(x)):
    norme[i].append(m.sqrt(x[i]**2+y[i]**2))

print(norme)
# r* pour afficher des points
# afficher points sur un graphe
g.legend()
