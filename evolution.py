import csv
import matplotlib.pyplot as plt
donnees=[]
with open('installation_parc.csv',newline='') as csvfile:
    reader=csv.reader(csvfile, delimiter=',')
    for row in reader:
        donnees.append(row)
       
SOMsolaire= {annee: 0 for annee in range(2016, 2026)}
SOMeolienneterrestre= {annee: 0 for annee in range(2016, 2026)}
SOMeolienneenmer={annee: 0 for annee in range(2016, 2026)}
for row in donnees:
    try:
        if row[2]=="Solaire":
            SOMsolaire[int(row[0])]+=int(row[3])
        if row[2]=="Eolienne terrestre":
            SOMeolienneterrestre[int(row[0])]+=int(row[3])
        if row[2]=="Eolienne en mer":
            SOMeolienneenmer[int(row[0])]+=int(row[3])
    except(ValueError, IndexError):
        pass
   
x=range(len(SOMsolaire))
width=0.25
plt.bar(x,SOMeolienneterrestre.keys(),SOMeolienneterrestre.values(), width=width,color='green', label="Eolienne terrestre")  
plt.bar([i+width for i in x],SOMeolienneenmer.keys(),SOMeolienneenmer.values(),width=width,color='blue', label="Eolienne en mer")  
plt.bar([i+2*width for i in x ],SOMsolaire.keys(),SOMsolaire.values(),width=width,color='red', label="Solaire")
plt.xticks([i+width for i in x],SOMeolienneterrestre.keys())
plt.xlabel('Année')
plt.ylabel('Émissions de CO₂ (Millions de Tonnes)')
plt.title("Évolution du parc installé d'électricité (renouvelable) en Europe ")
plt.grid(True)
plt.show()
import csv
import matplotlib.pyplot as plt
donnees=[]
with open('CO2.csv',newline='') as csvfile:
    reader=csv.reader(csvfile, delimiter=',')
    for row in reader:
        donnees.append(row)

#emissions gaz a effet de serre par pays de l'UE
donnees = donnees[1:]
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
        valeur = int(row[3])
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
{annee: 0 for annee in range(2016, 2026)}


plt.figure(figsize=(12, 6))


plt.plot(list(SOMallemagne.keys()), SOMallemagne.values(), marker='o', color='green', label='Allemagne')
plt.plot(list(SOMfrance.keys()), SOMfrance.values(), marker='o', color='purple', label='France')
plt.plot(list(SOMsuede.keys()), SOMsuede.values(), marker='o', color='orange', label='Suède')
plt.plot(list(SOMroumanie.keys()), SOMroumanie.values(), marker='o', color='pink', label='Roumanie')
plt.plot(list(SOMportugal.keys()), SOMportugal.values(), marker='o', color='brown', label='Portugal')
plt.plot(list(SOMpologne.keys()), SOMpologne.values(), marker='o', color='cyan', label='Pologne')
plt.plot(list(SOMnorvege.keys()),SOMnorvege.values(), marker='o', color='grey', label='Norvège')
plt.plot(list(SOMpaysbas.keys()), SOMpaysbas.values(), marker='o', color='olive', label='Pays-Bas')
plt.plot(list(SOMitalie.keys()), SOMitalie.values(), marker='o', color='navy', label='Italie')
plt.plot(list(SOMhongrie.keys()), SOMhongrie.values(), marker='o', color='teal', label='Hongrie')
plt.plot(list(SOMcroatie.keys()), SOMcroatie.values(), marker='o', color='gold', label='Croatie')
plt.plot(list(SOMgrece.keys()),SOMgrece.values(), marker='o', color='coral', label='Grèce')
plt.plot(list(SOMfinlande.keys()), SOMfinlande.values(), marker='o', color='darkred', label='Finlande')
plt.plot(list(SOMespagne.keys()), SOMespagne.values(), marker='o', color='darkgreen', label='Espagne')

plt.plot(list(SOMrepubliquetcheque.keys()), SOMrepubliquetcheque.values(), marker='o', color='brown', label='République Tchèque')

plt.plot(list(SOMbelgique.keys()),SOMbelgique.values(), marker='o', color='grey', label='Belgique')
plt.plot(list(SOMautriche.keys()), SOMautriche.values(), marker='o', color='green', label='Autriche')
plt.plot(list(SOMestonie.keys()), SOMestonie.values(), marker='o', color='darkblue', label='Estonie')
plt.plot(list(SOMdanemark.keys()), SOMdanemark.values(), marker='o', color='violet', label='Danemark')
plt.plot(list(SOMslovaquie.keys()), SOMslovaquie.values(), marker='o', color='b', label='Slovaquie')
plt.plot(list(SOMslovenie.keys()), SOMslovenie.values(), marker='o', color='r', label='Slovénie')
plt.plot(list(SOMlettonie.keys()), SOMlettonie.values(), marker='o', color='magenta', label='Lettonie')
plt.plot(list(SOMlituanie.keys()),SOMlituanie.values(), marker='o', color='lime', label='Lituanie')
plt.plot(list(SOMbulgarie.keys()), SOMbulgarie.values(), marker='o', color='pink', label='Bulgarie')

plt.xlabel('Année')
plt.ylabel('Émissions de CO₂ (Millions de Tonnes)')
plt.title("Émissions de gaz à effet de serre liées à la production d'électricité en Europe")
plt.grid(True)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')  # légende sur le côté pour plus de clarté
plt.tight_layout()
plt.show()

print("Lituanie :", SOMlituanie)




#total de CO2 dans L'UE
SOMTOTALE={annee: 0 for annee in range(2016, 2026)}
for row in donnees:
    try:
        if row[2]=="Emissions":
            print(row)
            SOMTOTALE[int(row[0][:4])]+=(int(row[3]))
    except (ValueError, IndexError):
        pass
print(SOMTOTALE)
plt.bar(SOMTOTALE.keys(),SOMTOTALE.values(),color='purple', label="emission totale")  
plt.xlabel('Année')
plt.ylabel('Émissions de CO₂ (Millions de Tonnes)')
plt.title("Émissions de gaz à effet de serre liées à la production d'électricité en Europe")
plt.grid(True)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()
