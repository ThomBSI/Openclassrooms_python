# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 15:47:40 2017

@author: thoma
"""

notes = [5,1,8,9,14]


mini = notes[0]
maxi = notes[0]
somme = 0
nb = 0
for note in notes:
    if note < mini:
        mini = note
    if note > maxi:
        maxi = note
    somme = somme + note
    nb+=1
moy = somme / nb
print("Note la plus basse : ",mini)
print("Note la plus haute : ",maxi)
print("Moyenne : ",moy)
print()
if moy < 10:
    print("T'es mauvais Jack !")
elif moy <12:
    print("assez bien")
elif moy <14:
    print("bien")
elif moy <16:
    print("très bien")
else:
    print("Excellent !")