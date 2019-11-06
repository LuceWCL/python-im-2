# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 09:04:43 2019

@author: Lucie
"""

"""Écrire un script python qui lit un fichier ligne par ligne et affiche pour chaque ligne

    a si la ligne contient la chaîne spam
    b si la ligne contient au plus 5 caractères et finit par un z
    Si la ligne contient une adresse mail de la forme x.y@z.t, afficher cette adresse
    d si les trois premiers caractères sont les mêmes que les trois derniers et dans le même ordre
    e si la ligne est un palindrôme, i.e. si la lire de gauche à droite ou de droite à gauche donne le même résultat, e.g. pyttyp
    NOPE sinon
"""

import re

with open("7.0-testcase.txt", "r",encoding="utf-8") as file:
    for ligne in file:
        lignes = ligne.strip()
#        print(len(line))
        if "spam" in lignes:
            print("a")
        if len(lignes)>=5 and lignes.endswith("z")==True:
            print("b")
        mail = re.search(r'(\w+\.\w+\@\w+\.\w+)',lignes)
        if mail is not None:
            print(mail.group(1))
        