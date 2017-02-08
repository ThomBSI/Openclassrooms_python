# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 14:51:24 2017

@author: thoma
"""


def table(nb, max=10):
    """Fonction affichant la table de multiplication par nb de
    1 * nb jusqu'Ã  max * nb"""
    i = 0
    while i < max:
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1