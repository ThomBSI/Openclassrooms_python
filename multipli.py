# -*- coding: latin-1 -*-

"""module multipli contenant la fonction table"""

def table(nb, max=10):
    """Fonction affichant la table de multiplication par nb de
    1 * nb jusqu'Ã  max * nb"""
    i = 0
    while i < max:
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1

# test de la fonction table
if __name__ == "__main__":
    table(4)

#__name__ vaux "__main__" si le fichier est appelé directement
