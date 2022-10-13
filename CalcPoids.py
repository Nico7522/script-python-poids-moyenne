fichier = open("E:\\Poids et programmes\\poids2.txt", "a")

faireMoyenne = False
date = input("Date : ")
poids = input("Poids : ")

faireMoyenne = input("Faire la moyenne ? ")

if(faireMoyenne == "oui"):
    faireMoyenne = True
    fichier.write(date)
    fichier.write(" : ")
    fichier.write(poids)
    fichier.write(' ')
else:
    faireMoyenne = False
    fichier.write(date)
    fichier.write(" : ")
    fichier.write(poids)
    fichier.write("\n")
fichier.close()

tab = []
tab2 = []

file = open("E:\\Poids et programmes\\poids2.txt", "r")
lines = file.readlines()
file.close()

for line in lines:
    tab.append(line.split())
    
tab = tab[-7:]

i = 0
while (i < len(tab)):
    tab2.append(tab[i][3])
    print(tab2[i])
    i = i + 1
    
somme = 0
i = 0
while (i < len(tab2)):
    somme = somme + float(tab2[i])
    print(tab2[i])
    i = i + 1
   
moyenne = somme / 7
# print(" Dimanche :",tab2[0],"\n","Lundi :",tab2[1],"\n","Mardi :",tab2[2],"\n","Mercredi :",tab2[3],"\n","Jeudi :",tab2[4],"\n","Vendredi :",tab2[5],"\n", "Samedi :",tab2[6])
print("La moyenne des 7 derniers jours est : ", round(moyenne, 2), "kg")



if(faireMoyenne == True):
    fichier = open("E:\\Poids et programmes\\poids2.txt", "a")
    fichier.write(" / Moyenne : ")
    fichier.write(str(moyenne))
    fichier.write("\n")
    fichier.close()

wait = input("Appuyez sur un bouton pour quitter...")





