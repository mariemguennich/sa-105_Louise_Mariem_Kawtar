import csv
import matplotlib.pyplot as plt
 
table = []
with open('Production_allemagne.csv', newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        table.append(row)
 
# Supprimer l'en-tête
del table[0]
 
production = {}
 
for i in range(len(table)):
    if len(table[i]) < 4:
        continue
 
    pays = table[i][1].strip()
    if pays != "Espagne":  # Changement ici pour l'Espagne
        continue
 
    annee = int(table[i][0][:4])
    filiere = table[i][2].strip()
    valeur_str = table[i][3].strip()
 
    if valeur_str == "":
        valeur = 0
    else:
        valeur = float(valeur_str.replace(",", "."))
 
    if annee not in production:
        production[annee] = {"Solaire": 0, "Eolien terrestre": 0}
 
    if filiere == "Solaire":
        production[annee]["Solaire"] += valeur
    elif filiere == "Eolien terrestre":
        production[annee]["Eolien terrestre"] += valeur
 
annees = sorted(production.keys())
solaire = [production[a]["Solaire"] for a in annees]
eolien = [production[a]["Eolien terrestre"] for a in annees]
 
plt.plot(annees, solaire, marker="o", label="Solaire")
plt.plot(annees, eolien, marker="s", label="Éolien terrestre")
plt.xlabel("Année")
plt.ylabel("Production (TWh)")
plt.title("Production d'électricité en Espagne")
plt.legend()
plt.grid()
plt.show()



