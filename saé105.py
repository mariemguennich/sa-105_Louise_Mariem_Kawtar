
import csv
import matplotlib.pyplot as plt
donneesS=[]
with open('productionsolaire.csv',newline='', encoding='latin-1') as csvfile:
    reader=csv.reader(csvfile, delimiter=';')
    for row in reader:
        donneesS.append(row)
del donneesS[0]
donneesE=[]
with open('productioneolienne.csv',newline='', encoding='latin-1') as csvfile:
    reader=csv.reader(csvfile, delimiter=';')
    for row in reader:
        donneesE.append(row)
del donneesE[0]
print(donneesS)
print(donneesE)

valeur1 = []
valeur2 = []

#il faut changer les , par des .
for i in range (len(donneesS)):
    S=donneesS[i][2]
    if ',' in S:
        ps=S.split(',')
        valeur1.append(float(ps[0]+"."+ps[1]))
#de meme dans les valeurs de la production eolienne

for m in range (len(donneesE)):
    E=donneesE[m][2]
    if ',' in E:
        pe=E.split(',')
        valeur2.append(float(pe[0]+"."+pe[1]))
annees=[2007+i for i in range(18)]
"""for ligne in donneesE:
    annee = int(ligne[0][:4])
    annees.append(annee)
"""   
moyennes = {}

for i in range(len(annees)):
    annee = annees[i]
    valeurS = valeur1[i]
    valeurE=valeur2[i]
    if annee not in moyennes:
        moyennes[annee] = []
    moyennes[annee].append(valeurS)
annees_uniques = []
valeurs_moyennes = []
valeure_moyennes=[]
for annee in moyennes:
    annees_uniques.append(annee)
    valeurs_moyennes.append(sum(moyennes[annee]) / len(moyennes[annee]))
    valeure_moyennes.append(sum(moyennes[annee]) / len(moyennes[annee]))

 
print(len(valeurs_moyennes))
print(len(valeure_moyennes))
print(len(annees))  
 
plt.plot(annees_uniques,valeurs_moyennes)
plt.plot(annees_uniques,valeure_moyennes)
plt.xlabel("Année")
plt.ylabel("Production solaire et eolienne")
plt.title("Comparaison entre le production eolienne et la production solaire")
plt.show()
