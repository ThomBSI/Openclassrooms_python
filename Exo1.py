# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 15:19:25 2017

@author: thoma
"""

joursSemaine = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]

    
i = 0
while i<7:
    print(joursSemaine[i]," : ")
    if i<4:
        print("au travail !")
    elif i==4:
        print("Chouette c'est vendredi !")
    else:
        print("Repos ce week end !")
    i+=1
    print()