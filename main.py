if __name__ == "__main__":

   # I.Création d'une liste qui contient 10 éléments 

   noms=['Ngabirano','Niyongabo','Igiraneza','Musobwa','Niyukuri','Bizindavyi','Nziza','Niyuhire','Irakoze','Ayinkamiye']

   # 1. Affichage des éléments qui se trouve sur la liste 
   print("----Afficher des éléments qui se trouve sur la premiére liste----")

   for i in noms:
       print(i)
   

# 2. Changement de contenu  de l'élément numéro 5
print("----Changer le contenu  de l'élément numéro 5----")

noms[4]='Ngabire'

for i in noms:
    print(i)

# 3. Créer une nouvelle liste en la remplissant avec les éléments de la liste précédente contenant la lettre "a"
print("----Créer une nouvelle liste en la remplissant avec les éléments de la liste précédentecontenant la lettre a-----")

Noms=[]

# Prendre les éléments de la premiére liste contenant la lettre "a" et les mettre sur la nouvelle liste
for i in noms:
    if "a" in i:
        Noms.append(i)

# Afficher les nouvelles éléments sur la nouvelle liste
for j in Noms:
    print(j)

# 4. Ajouter un élément à la fin de la liste
print("----Ajouter un élément à la fin de la liste----")

noms.append('Akimana')

# Afficher la liste contenant une nouvelle élément ajouter à la fin de la liste 
for i in noms:
    print(i)

# 5.  Ajouter un élément à l’index numéro 2
print("----Ajouter un élément à l’index numéro 2----")

noms.insert(2, 'Akimana')

# Afficher la liste contenant une nouvelle élément Ajouter à l’index numéro 2 
for i in noms:
    print(i)

# 6. Supprimer l'élément numéro 3
print("------Supprimer l'élément numéro 3-----")

del noms[2]

# Afficher une nouvelle liste après avoir supprimer l'élément numéro 3
for i in noms:
    print(i)

# 7. Supprimer l'élément à l’index numéro 2
print("------Supprimer l'élément à l’index numéro 2-----")

del noms[2]

# Afficher une nouvelle liste après avoir Supprimer l'élément à l’index numéro 2
for i in noms:
    print(i)

# 8.  Ordonner la liste
print("---- Ordonner la liste----")
 
noms.sort()

# Afficher une liste bien ordonnée
for i in noms:
    print(i)

# 9. Afficher la sens au sens inverse
print("----Afficher la sens au sens inverse----")

noms.reverse()

# Afficher une liste au sens inverse
for i in noms:
    print(i)

# 10. Vider la liste
print("----Vider la liste----")

noms.clear()

# Afficher la liste vide
for i in noms:
    print(i)

# 11.  Supprimer la liste
print("---- Supprimer la liste----")

# Suppression d'une liste
del noms

#--------------------------------------------------------------------------------------------------------------------------

# II.Création d'une  tuple qui contient 10 éléments

numero=(101,201,3,40,50,3,370,80,909,100)

print("-----Afficher les éléments de la tuple-----")

# Affichage des éléments de la tuple
for i in numero:
    print(i)

# 1. Afficher le nombre de fois la valeur 3 apparait dans la tuple
print("----Afficher le nombre de fois la valeur 3 apparait dans la tuple----")

index =0
Val =numero[0]
for i in range(len(numero)):
    n=numero[i]
    if n==3:
        index+=1
print("Le nombre de fois que la valeur 3 apparait dans la tuple est : "+str(index))

# 2.  Afficher le contenu de l'élément numéro 5
print("---- Afficher le contenu de l'élément numéro 5----")

element_5 = numero[4]
print(element_5)

# 3. Ordonner la tuple
print("----Ordonner la tuple----")

# Afficher la tuple ordonnée
numero_ordonnee = sorted(numero)
print(numero_ordonnee)

# 4. Ajouter un élément à la fin de la tuple
print("----Ajouter un élément à la fin de la tuple-----")

numero_original = numero

# Numéro ajouter à la fin
numero += (4,)
print(numero)

# 5. Ajouter un élément à l’index numéro 3
print("-----Ajouter un élément à l’index numéro 3----")

# Changer une tuple en une liste
numero_list = list(numero)
print(numero_list)

# Ajouter un nouveau élément à l’index numéro 3
numero_list.insert(3, 707)

#Afficher une liste apres avoir insert un nouveau élément sur l’index numéro 3
print("-----Afficher une nouvelle liste apres avoir changer la tuple en une liste----")
for i in numero_list:
    print(i)

#Changer une liste en une tuple apres avoir insert un nouveau élément sur l’index numéro 3
numero_tuple = tuple(numero_list)

#Afficher une tuple apres avoir insert un nouveau élément sur l’index numéro 3
print("-----Afficher une nouvelle tuple apres avoir changer la liste en une tuple----")
for i in numero_tuple:
    print(i)

# 6. Afficher la nouvelle tuple
print("-----Afficher la nouvelle tuple-----")
  
nouvelle_tuple=numero_tuple
print(nouvelle_tuple)

# III.Création d'un set qui contient 10 éléments

marque_ordinateur={"Fujistu","Acer","Asus","Dell","HP","Huawei","Lenovo","MSI","Razer","Apple"}

# 1. Afficher le set
print("----Affichage d'un set----")

for i in marque_ordinateur:
    print(i)

# 2.  Ajouter un élément
print("----Ajouter un élément----")

# Ajouter un nouveau élément
marque_ordinateur.add("Toshiba")

# Affichage apres avoir ajout un élément
for i in marque_ordinateur:
    print(i)

# 3. Supprimer un élément
print("-----Supprimer un élément-----")

# Suppression d'un élément
marque_ordinateur.remove("Razer")

# Affichage apres avoir supprimer un élément
for i in marque_ordinateur:
    print(i)

# 4. Supprimer le set
print("-----Supprimer le set-----")

# Suppression de set
del marque_ordinateur

# IV.Création d'un dictionnaire qui contient 10 éléments

fichier_etudiant={"Nom":"Ngabirano", "Prenom":"Guy Michel", "Telephone":"+257868689", 
                  "Etat_Civil":"Celibataire", "Date_Naissance":"1/7/2000", "Lieu_Naissance":"Ngagara", 
                  "Domicilité":"Ngagara", "Travail":"Etudiant", "Faculté":"Inforamtique",
                  "Departement":"Genie Logiciel"}

# 1. Afficher le dictionnaire
print("----Afficher le dictionnaire----")

print(fichier_etudiant)

# 2. Afficher seulement les clés
print("-------Affichage des clés seulement-------")

for i in fichier_etudiant.keys():
    print(i)

# 3. Afficher seulement les valeurs
print("-------Affichage des valeurs seulement-------")

for i in fichier_etudiant.values():
    print(i)

# 4. Afficher les clés et les valeurs sous le format : Clé : Valeur
print("-------Affichage des clés et des valeurs sous le format : Clé : Valeur-------")

for i,j in fichier_etudiant.items():
    print(f"{i} : {j}")

# 5. Supprimer l'élément à la clé numéro 2
print("-----Supprimer l'élément à la clé numéro 2-----")

# Suppression d'élément qui se trouve à la clé numéro 2
key = "Prenom"
del fichier_etudiant[key]

# Affichage apres avoir supprimer l'élément qui se trouve à la clé numéro 2
print(fichier_etudiant)