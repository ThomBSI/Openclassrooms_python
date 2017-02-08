# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 15:00:27 2017

@author: thoma
"""

annee = input("Saisissez une année supérieure à 0 :")
try:
    annee = int(annee) # Conversion de l'année
    assert annee > 0
except ValueError as _e:
    print("Vous n'avez pas saisi un nombre.",_e)
except AssertionError as _e:
    print("L'année saisie est inférieure ou égale à 0.", _e)