#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""ProjetsPics.py - Fichiers de visualisation des données sous formes de graphiques
des fichiers (Chaussures.csv, Origine.csv, Pic.csv, Sommet.csv)."""

__author__ = "Colas Naudi, Mathis Heriveau"
__version__ = "1.0"
__date__ = "2022-05-12"

# ~~~~~~~~~~~~~~~~~~~~~~~~~ Import des bibliothèques ~~~~~~~~~~~~~~~~~~~~~~~~~ #

import pandas as pd
import matplotlib.pyplot as plt

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Import des fichiers ~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
fic_chaussures = pd.read_table(
        "Fichiers/Chaussures.csv",
        decimal = ",",
        sep = ";"
)

fic_pic = pd.read_table(
        "Fichiers/Pic.csv",
        decimal = ",",
        sep = ";"
)

fic_origines = pd.read_table(
        "Fichiers/Origine.csv",
        decimal = ",",
        sep = ";"
)

fic_sommets = pd.read_table(
        "Fichiers/Sommet.csv",
        decimal = ",",
        sep = ";"
)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
#                               Analyse bivariée                               #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# ~~~~~~~~~~~~~~ Répartition des sexes en fonction du pic gravis ~~~~~~~~~~~~~ #
def graph1():
        Sexe = fic_pic['Sexe']

        corresp = {'Aneto' : 'Aneto',
                'Aragüells' : 'Autre',
                'Aspe' : 'Autre',
                'Bachimala' : 'Autre',
                'Bacías' : 'Autre',
                'Bisaurín' : 'Bisaurín',
                'Castillo de Acher' : 'Castillo de Acher',
                'Cilindro' : 'Autre',
                'Collarada' : 'Autre',
                'Cotiella' : 'Autre',
                'Garmo Negro' : 'Garmo Negro',
                'Infiernos' : 'Autre',
                'La Facha' : 'Autre',
                'La Munia' : 'Autre',
                'Monte Perdido' : 'Monte Perdido',
                'Mulleres' : 'Autre',
                'Petrechema' : 'Petrechema',
                'Peña Forca' : 'Autre',
                'Pico de Alba' : 'Autre',
                'Posets' : 'Posets',
                'Punta Escuzana' : 'Autre',
                'Punta Las Olas' : 'Autre',
                'Punta Suelza' : 'Autre',
                'Robiñera' : 'Autre',
                'Tendeñera' : 'Autre',
                'Vallibierna' : 'Vallibierna'
        }

        fic_pic['pico'] = fic_pic['pico'].map(corresp)

        Pico = fic_pic['pico']

        SexePico = pd.crosstab(Pico, Sexe, normalize="index")

        SexePico.sort_values("F", ascending=False).plot(
                kind="bar",
                stacked=True
        )

        plt.xticks(rotation=70)
        plt.xlabel('')

        plt.legend(bbox_to_anchor =(1, 1), ncol = 1)

        plt.title("Répartition des sexes en fonction du pic gravis")

# ~~~~~~~~ Altitude moyenne en fonction du sommet (Diagramme en barre) ~~~~~~~ #

def graph2():
        Vallee = fic_sommets['Zone (Carte)']

        df = fic_sommets

        Altitude = df.groupby(['Zone (Carte)']).mean()

        df_sorted_desc = df.sort_values('Altitude', ascending=False)

        plt.bar('Zone (Carte)', 'Altitude',data=df_sorted_desc)

        plt.title("Altitude moyenne en fonction de la vallée")

        plt.legend(['Altitude'])

        plt.xticks(rotation=30)

# ~~~~~~~~ Altitude moyenne en fonction du sommet (Boîte à moustache) ~~~~~~~~ #

def graph3():
        df = fic_sommets

        g = df.groupby("Zone (Carte)")

        df = pd.DataFrame({col: val['Altitude'] for col, val in g})

        median = df.median()

        median.sort_values(ascending=False, inplace=True)

        df = df[median.index]

        df.boxplot()

        plt.title("Altitude moyenne en fonction de la vallée")

        plt.xticks(rotation=45)

        plt.show()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
#                              Programme principal                             #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

num = int(input("Entrer le numéro de l'analyse à effectuer : \n- 0 : Quitter\n- 1 : Répartition des sexes en fonction du pic gravis\n- 2 : Altitude moyenne en fonction du sommet (Diagramme en barre)\n- 3 : Altitude moyenne en fonction du sommet (Boîte à moustache)\n\nVotre choix : "))
if(num >= 1 or num <= 3):
        if num == 1:
                graph1()
        elif num == 2:
                graph2()
        elif num == 3:
                graph3()