import pandas as pd
import matplotlib.pyplot as plt
import csv
annees = []
production = []
consommation = []

donneesS = []
donneesE = []
donneesC = []

# SOLAIRE
with open('productionsolaire.csv', newline='', encoding='latin-1') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        donneesS.append(row)

del donneesS[0]

for ligne in donneesS:
    if ligne[2] == "":
        continue

    valeur = ligne[2]
    if ',' in valeur:
        p = valeur.split(',')
        solaire = float(p[0] + "." + p[1])
    else:
        solaire = float(valeur)

    production.append(solaire)

# ÉOLIEN (on l'ajoute a la production solaire)
with open('productioneolienne.csv', newline='', encoding='latin-1') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        donneesE.append(row)

del donneesE[0]

i = 0
for ligne in donneesE:
    if i >= len(production):
        break

    if ligne[2] == "":
        i += 1
        continue

    valeur = ligne[2]
    if ',' in valeur:
        p = valeur.split(',')
        eolien = float(p[0] + "." + p[1])
    else:
        eolien = float(valeur)

    production[i] = production[i] + eolien
    i += 1

# CONSOMMATION
with open('Consommationbrute.csv', newline='', encoding='latin-1') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        donneesC.append(row)

del donneesC[0]

for ligne in donneesC:
    if ligne[3] == "":
        continue

    valeur = ligne[3]
    if ',' in valeur:
        p = valeur.split(',')
        c = float(p[0] + "." + p[1])
    else:
        c = float(valeur)

    consommation.append(c)

    annee = int(ligne[0][0:4])
    annees.append(annee)

# ANNÉES UNIQUES
annees_uniques = []
for a in annees:
    if a not in annees_uniques:
        annees_uniques.append(a)

# MOYENNES PAR ANNÉE
prod_moyenne = []
cons_moyenne = []

for a in annees_uniques:
    s_prod = 0
    s_cons = 0
    k = 0

    for i in range(len(production)):
        if annees[i] == a:
            s_prod += production[i]
            s_cons += consommation[i]
            k += 1

    prod_moyenne.append(s_prod / k)
    cons_moyenne.append(s_cons / k)

# graphique en barres groupées
x = range(len(annees_uniques))
largeur = 0.4

plt.bar(x, prod_moyenne, width=largeur, label="Production")
plt.bar([i + largeur for i in x], cons_moyenne, width=largeur, label="Consommation")

plt.xticks([i + largeur / 2 for i in x], annees_uniques)
plt.xlabel("Année")
plt.ylabel("Énergie (TWh)")
plt.title("Production renouvelable vs consommation en Europe")
plt.legend()
plt.grid(True)
plt.show()
