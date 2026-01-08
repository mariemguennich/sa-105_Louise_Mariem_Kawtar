import csv
import matplotlib.pyplot as plt
donnees=[]
with open('CO2.csv',newline='', encoding='latin-1') as csvfile:
    reader=csv.reader(csvfile, delimiter=',')
    for row in reader:
        donnees.append(row)


donnees = donnees[1:]
#SOM = {annee: 0 for annee in range(2016, 2026)}
SOMslovaquie= {annee: 0 for annee in range(2016, 2026)}
SOMslovenie={annee: 0 for annee in range(2016, 2026)}
SOMallemagne={annee: 0 for annee in range(2016, 2026)}
SOMfrance={annee: 0 for annee in range(2016, 2026)}
SOMsuede={annee: 0 for annee in range(2016, 2026)}
SOMroumanie={annee: 0 for annee in range(2016, 2026)}
SOMportugal={annee: 0 for annee in range(2016, 2026)}
SOMpologne={annee: 0 for annee in range(2016, 2026)}
SOMnorvege={annee: 0 for annee in range(2016, 2026)}
SOMpaysbas={annee: 0 for annee in range(2016, 2026)}
SOMlettonie={annee: 0 for annee in range(2016, 2026)}
SOMlituanie={annee: 0 for annee in range(2016, 2026)}
SOMitalie={annee: 0 for annee in range(2016, 2026)}
SOMhongrie={annee: 0 for annee in range(2016, 2026)}
SOMcroatie={annee: 0 for annee in range(2016, 2026)}
SOMgrece={annee: 0 for annee in range(2016, 2026)}
SOMfinlande={annee: 0 for annee in range(2016, 2026)}
SOMespagne={annee: 0 for annee in range(2016, 2026)}
SOMestonie={annee: 0 for annee in range(2016, 2026)}
SOMdanemark={annee: 0 for annee in range(2016, 2026)}
SOMrepubliquetcheque={annee: 0 for annee in range(2016, 2026)}
SOMbulgarie={annee: 0 for annee in range(2016, 2026)}
SOMbelgique={annee: 0 for annee in range(2016, 2026)}
SOMautriche={annee: 0 for annee in range(2016, 2026)}

for row in donnees:
    try:
        annee = int(row[0][:4])  
        valeur = int(row[4])
        if row[2]=='Emissions' and row[1]=="Slovaquie":
            SOMslovaquie[annee]+= valeur
        if row[2]=='Emissions' and row[1]=="Slovénie":
            SOMslovenie[annee]+= valeur
        if row[2]=='Emissions' and row[1]=="Autriche":
            SOMautriche[annee]+= valeur
        if row[2]=='Emissions' and row[1]=="Belgique":
            SOMbelgique[annee]+= valeur
        if row[2]=='Emissions' and row[1]=="Bulgarie":
            SOMbulgarie[annee]+= valeur
        if row[2]=='Emissions' and row[1]=="République tchèque":
            SOMrepubliquetcheque[annee]+= valeur
        if row[2]=='Emissions' and row[1]=="Danemark":
            SOMdanemark[annee]+= valeur
        if row[2]=='Emissions' and row[1]=="Estonie":
            SOMestonie[annee]+= valeur
        if row[2]=='Emissions' and row[1]=="Espagne":
            SOMespagne[annee]+= valeur
        if row[2]=='Emissions' and row[1]=="Finlande":
            SOMfinlande[annee]+= valeur
        if row[2]=='Emissions' and row[1]=="Grèce":
            SOMgrece[annee]+= valeur
        if row[2]=='Emissions' and row[1]=="Croatie":
            SOMcroatie[annee]+= valeur
        if row[2]=='Emissions' and row[1]=="Hongrie":
            SOMhongrie[annee]+= valeur
        if row[2]=='Emissions' and row[1]=="Italie":
            SOMitalie[annee]+= valeur
        if row[2]=='Emissions' and row[1]=="Lettonie":
            SOMlettonie[annee]+= valeur
        if row[2]=='Emissions' and row[1]=="Lituanie":
            SOMlituanie[annee]+= valeur
        if row[2]=='Emissions' and row[1]=="Pays-Bas":
            SOMpaysbas[annee]+= valeur
        if row[2]=='Emissions' and row[1]=="Norvège":
            SOMnorvege[annee]+= valeur
        if row[2]=='Emissions' and row[1]=="Pologne":
            SOMpologne[annee]+= valeur
        if row[2]=='Emissions' and row[1]=="Portugal":
            SOMportugal[annee]+= valeur
        if row[2]=='Emissions' and row[1]=="Roumanie":
            SOMroumanie[annee]+= valeur
        if row[2]=='Emissions' and row[1]=="Suède":
            SOMsuede[annee]+= valeur
        if row[2]=='Emissions' and row[1]=="France":
            SOMfrance[annee]+= valeur
        if row[2]=='Emissions' and row[1]=="Allemagne":
            SOMallemagne[annee]+= valeur
    except (ValueError, IndexError):
        pass

def conversion(dico):
    valeur_dico=[v / 1000000 for v in dico.values()]
    return valeur_dico



plt.figure(figsize=(12, 6))


plt.plot(list(SOMallemagne.keys()), conversion(SOMallemagne), marker='o', color='green', label='Allemagne')
plt.plot(list(SOMfrance.keys()), conversion(SOMfrance), marker='o', color='purple', label='France')
plt.plot(list(SOMsuede.keys()), conversion(SOMsuede), marker='o', color='orange', label='Suède')
plt.plot(list(SOMroumanie.keys()), conversion(SOMroumanie), marker='o', color='pink', label='Roumanie')
plt.plot(list(SOMportugal.keys()), conversion(SOMportugal), marker='o', color='brown', label='Portugal')
plt.plot(list(SOMpologne.keys()), conversion(SOMpologne), marker='o', color='cyan', label='Pologne')
plt.plot(list(SOMnorvege.keys()), conversion(SOMnorvege), marker='o', color='grey', label='Norvège')
plt.plot(list(SOMpaysbas.keys()), conversion(SOMpaysbas), marker='o', color='olive', label='Pays-Bas')
plt.plot(list(SOMitalie.keys()), conversion(SOMitalie), marker='o', color='navy', label='Italie')
plt.plot(list(SOMhongrie.keys()), conversion(SOMhongrie), marker='o', color='teal', label='Hongrie')
plt.plot(list(SOMcroatie.keys()), conversion(SOMcroatie), marker='o', color='gold', label='Croatie')
plt.plot(list(SOMgrece.keys()), conversion(SOMgrece), marker='o', color='coral', label='Grèce')
plt.plot(list(SOMfinlande.keys()), conversion(SOMfinlande), marker='o', color='darkred', label='Finlande')
plt.plot(list(SOMespagne.keys()), conversion(SOMespagne), marker='o', color='darkgreen', label='Espagne')

plt.plot(list(SOMrepubliquetcheque.keys()), conversion(SOMrepubliquetcheque), marker='o', color='brown', label='République Tchèque')

plt.plot(list(SOMbelgique.keys()), conversion(SOMbelgique), marker='o', color='grey', label='Belgique')
plt.plot(list(SOMautriche.keys()), conversion(SOMautriche), marker='o', color='green', label='Autriche')
plt.plot(list(SOMestonie.keys()), conversion(SOMestonie), marker='o', color='darkblue', label='Estonie')
plt.plot(list(SOMdanemark.keys()), conversion(SOMdanemark), marker='o', color='violet', label='Danemark')
plt.plot(list(SOMslovaquie.keys()), conversion(SOMslovaquie), marker='o', color='b', label='Slovaquie')
plt.plot(list(SOMslovenie.keys()), conversion(SOMslovenie), marker='o', color='r', label='Slovénie')
plt.plot(list(SOMlettonie.keys()), conversion(SOMlettonie), marker='o', color='magenta', label='Lettonie')
plt.plot(list(SOMlituanie.keys()), conversion(SOMlituanie), marker='o', color='lime', label='Lituanie')
plt.plot(list(SOMbulgarie.keys()), conversion(SOMbulgarie), marker='o', color='pink', label='Bulgarie')

plt.xlabel('Année')
plt.ylabel('Émissions de CO₂ (Millions de Tonnes)')
plt.title("Émissions de gaz à effet de serre liées à la production d'électricité en Europe")
plt.grid(True)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')  # légende sur le côté pour plus de clarté
plt.tight_layout()
plt.show()
"""
plt.plot(list(SOMestonie.keys()), conversion(SOMestonie), marker='o', color='darkblue', label='Estonie')
plt.plot(list(SOMdanemark.keys()), conversion(SOMdanemark), marker='o', color='violet', label='Danemark')
plt.plot(list(SOMslovaquie.keys()), conversion(SOMslovaquie), marker='o', color='b', label='Slovaquie')
plt.plot(list(SOMslovenie.keys()), conversion(SOMslovenie), marker='o', color='r', label='Slovénie')
plt.plot(list(SOMlettonie.keys()), conversion(SOMlettonie), marker='o', color='magenta', label='Lettonie')
plt.plot(list(SOMlituanie.keys()), conversion(SOMlituanie), marker='o', color='lime', label='Lituanie')
plt.plot(list(SOMbulgarie.keys()), conversion(SOMbulgarie), marker='o', color='pink', label='Bulgarie')
plt.xlabel('Année')
plt.ylabel('Émissions de CO₂ (Millions de Tonnes)')
plt.title("Émissions de gaz à effet de serre liées à la production d'électricité en Europe")
plt.grid(True)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')  # légende sur le côté pour plus de clarté
plt.tight_layout()
plt.show()
"""
print("Slovaquie :", SOMslovaquie)
print("Slovénie :", SOMslovenie)
print("Allemagne :", SOMallemagne)
print("France :", SOMfrance)
print("Suède :", SOMsuede)
print("Roumanie :", SOMroumanie)
print("Portugal :", SOMportugal)
print("Pologne :", SOMpologne)
print("Norvège :", SOMnorvege)
print("Pays-Bas :", SOMpaysbas)
print("Lettonie :", SOMlettonie)
print("Lituanie :", SOMlituanie)
print("Italie :", SOMitalie)
print("Hongrie :", SOMhongrie)
print("Croatie :", SOMcroatie)
print("Grèce :", SOMgrece)
print("Finlande :", SOMfinlande)
print("Espagne :", SOMespagne)
print("Estonie :", SOMestonie)
print("Danemark :", SOMdanemark)
print("République Tchèque :", SOMrepubliquetcheque)
print("Bulgarie :", SOMbulgarie)
print("Belgique :", SOMbelgique)
print("Autriche :", SOMautriche)
