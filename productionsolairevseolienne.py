
import csv
import matplotlib.pyplot as plt
donneesS = []
valeursS = []
anneesS = []

with open('productionsolaire.csv', newline='', encoding='latin-1') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        donneesS.append(row)

del donneesS[0]   # enlever l'en-tête

#donnees du production solaire 
for ligne in donneesS:
    if ligne[2] == "":
        continue
    S = ligne[2]
# il faut changer les , par des .
    if ',' in S:
        ps = S.split(',')
        valeur = float(ps[0] + "." + ps[1])
    else:
        valeur = float(S)

    valeursS.append(valeur)

# ANNÉES 
for ligne in donneesS:
    if ligne[2] == "":
        continue

    annee = int(ligne[0][0:4])
    anneesS.append(annee)

# donnees du production du l'éolienne
anneesE = []
valeursE = []
with open('productioneolienne.csv', newline='', encoding='latin-1') as f:
    reader = csv.reader(f, delimiter=';')
    next(reader)

    for row in reader:
        annee = int(row[0][:4])
        E = row[2]
# il faut changer les , par des .
        if ',' in E:
            pe = E.split(',')
            valeur = float(pe[0] + "." + pe[1])
        anneesE.append(annee)
        valeursE.append(valeur)

# MOYENNES SOLAIRE
moyennesS = {}
for i in range(len(anneesS)):
    a = anneesS[i]
    if a not in moyennesS:
        moyennesS[a] = []
    moyennesS[a].append(valeursS[i])

# MOYENNES ÉOLIEN
moyennesE = {}
for i in range(len(anneesE)):
    a = anneesE[i]
    if a not in moyennesE:
        moyennesE[a] = []
    moyennesE[a].append(valeursE[i])
    
# LISTES FINALES
annees = []
solaire = []
eolien = []

for a in moyennesS:
    if a in moyennesE:
        annees.append(a)
        solaire.append(sum(moyennesS[a]) / len(moyennesS[a]))
        eolien.append(sum(moyennesE[a]) / len(moyennesE[a]))
        
# TRI PAR ANNÉE
for i in range(len(annees)):
    for j in range(i + 1, len(annees)):
        if annees[j] < annees[i]:
            annees[i], annees[j] = annees[j], annees[i]
            solaire[i], solaire[j] = solaire[j], solaire[i]
            eolien[i], eolien[j] = eolien[j], eolien[i]

# AFFICHAGE
plt.plot(annees, solaire, label="Solaire")
plt.plot(annees, eolien, label="Éolien")
plt.xlabel("Année")
plt.ylabel("Production moyenne")
plt.title("Production solaire vs éolienne")
plt.legend()
plt.grid(True)
plt.show()
