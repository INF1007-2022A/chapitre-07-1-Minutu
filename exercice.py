#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import turtle
from math import pi

# TODO: Définissez vos fonction ici
def volume_masse_ellipsoide(a=1, b = 2, c = 3, massevolumique = 5):
    volume = 4/3 * pi * a * b * c

    return volume, volume*massevolumique

def arbre(mina, i):

    if i<10:
        return
    else:
        mina.forward(i)
        mina.left(45)
        arbre(mina, 2*i/3)
        mina.right(90)
        arbre(mina, 2*i/3)
        mina.left(45)
        mina.backward(i)

def valide_String(string):
    valid_letters = 'atgc'
    for i in string:
        if i in valid_letters:
            continue
        else:
            return False
    return True
def saisie(type):
    valeur = str(input(f'entrez une sequence valide {type}'))

    if valide_String(valeur):
        return valeur

    print(f'La {type} n"est pas valide')
    return saisie(type)

def proportion(chaine, sequence):
    longueur_initiale = len(chaine)
    chaine2= chaine.strip(sequence)
    longueur_finale = len(chaine2)
    print(f'Il y a {chaine.count(sequence)/len(chaine)*100:.2f} % de {sequence}')

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    proportion('attgcaatggtggtacatg', 'ca')

    pass
