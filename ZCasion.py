# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 16:00:49 2017

@author: thoma
"""

import random as r
import math as m

mise = input("Entrez votre mise : ")
try:
    numeroMise = input("Sur quel numéro voulez-vous miser (de 0 à 49) ? ")
    assert numeroMise<0 or numeroMise>49
    gain=0
    roulette = r.randrange(1,50)
    if numeroMise == roulette:
        gain = mise * 3
    elif numeroMise%2 == roulette%2:
        gain = mise + m.ceil(mise/2)
    else:
        gain = 0
    print("Résultats :")
    if gain != 0:
        print("Vous avez gagné ",gain," euros !")
    else:
        print("Vous n'avez rien gagné...")
except AssertionError:
    print("Vous n'avez pas saisi un numéro valide (entier entre 0 et 49)")
except as _e:
    print("Autre erreur : ",_e)