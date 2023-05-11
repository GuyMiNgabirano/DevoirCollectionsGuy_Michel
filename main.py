if __name__ == "__main__":

   # I.Création d'une liste qui contient 10 éléments 

   print("I.Creation d'une liste qui contient 10 elements\n")

   noms=['Ngabirano','Niyongabo','Igiraneza','Musobwa','Niyukuri','Bizindavyi','Nziza','Niyuhire','Irakoze','Ayinkamiye']

   # 1. Affichage des éléments qui se trouve sur la liste 
   print("----1. Afficher des elements qui se trouve sur la premiere liste----\n")

   for i in noms:
       print(i)
   

# 2. Changement de contenu  de l'élément numéro 5
print("----2. Changer le contenu  de l'element numero 5----\n")

noms[4]='Ngabire'

for i in noms:
    print(i)

# 3. Créer une nouvelle liste en la remplissant avec les éléments de la liste précédente contenant la lettre "a"
print("----3. Creer une nouvelle liste en la remplissant avec les elements de la liste precedentecontenant la lettre a-----\n")

Noms=[]

# Prendre les éléments de la premiére liste contenant la lettre "a" et les mettre sur la nouvelle liste
for i in noms:
    if "a" in i:
        Noms.append(i)

# Afficher les nouvelles éléments sur la nouvelle liste
for j in Noms:
    print(j)

# 4. Ajouter un élément à la fin de la liste
print("----4. Ajouter un element a la fin de la liste----\n")

noms.append('Akimana')

# Afficher la liste contenant une nouvelle élément ajouter à la fin de la liste 
for i in noms:
    print(i)

# 5.  Ajouter un élément à l’index numéro 2
print("----5. Ajouter un element a l’index numero 2----\n")

noms.insert(2, 'Akimana')

# Afficher la liste contenant une nouvelle élément Ajouter à l’index numéro 2 
for i in noms:
    print(i)

# 6. Supprimer l'élément numéro 3
print("------6. Supprimer l'element numero 3-----\n")

del noms[2]

# Afficher une nouvelle liste après avoir supprimer l'élément numéro 3
for i in noms:
    print(i)

# 7. Supprimer l'élément à l’index numéro 2
print("------7. Supprimer l'element a l’index numero 2-----\n")

del noms[2]

# Afficher une nouvelle liste après avoir Supprimer l'élément à l’index numéro 2
for i in noms:
    print(i)

# 8.  Ordonner la liste
print("----8. Ordonner la liste----\n")
 
noms.sort()

# Afficher une liste bien ordonnée
for i in noms:
    print(i)

# 9. Afficher la sens au sens inverse
print("----9.Afficher la sens au sens inverse----\n")

noms.reverse()

# Afficher une liste au sens inverse
for i in noms:
    print(i)

# 10. Vider la liste
print("----10. Vider la liste----\n")

noms.clear()

# Afficher la liste vide
for i in noms:
    print(i)

# 11.  Supprimer la liste
print("----11. Supprimer la liste----\n")

# Suppression d'une liste
del noms

#--------------------------------------------------------------------------------------------------------------------------
print("--------------------------------------------------------------------------------------------------------------------------\n")

# II.Création d'une  tuple qui contient 10 éléments

print("II.Creation d'une  tuple qui contient 10 elements\n")

numero=(101,201,3,40,50,3,370,80,909,100)

print("-----Afficher les elements de la tuple-----\n")

# Affichage des éléments de la tuple
for i in numero:
    print(i)

# 1. Afficher le nombre de fois la valeur 3 apparait dans la tuple
print("----1. Afficher le nombre de fois la valeur 3 apparait dans la tuple----\n")

index =0
Val =numero[0]
for i in range(len(numero)):
    n=numero[i]
    if n==3:
        index+=1
print("Le nombre de fois que la valeur 3 apparait dans la tuple est : "+str(index)+"\n")

# 2.  Afficher le contenu de l'élément numéro 5
print("----2. Afficher le contenu de l'element numero 5----\n")

element_5 = numero[4]
print(element_5)

# 3. Ordonner la tuple
print("----3. Ordonner la tuple----\n")

# Afficher la tuple ordonnée
numero_ordonnee = sorted(numero)
print(numero_ordonnee)

# 4. Ajouter un élément à la fin de la tuple
print("----4. Ajouter un element a la fin de la tuple-----\n")

numero_original = numero

# Numéro ajouter à la fin
numero += (4,)
print(numero)

# 5. Ajouter un élément à l’index numéro 3
print("-----5. Ajouter un element a l’index numero 3----\n")

# Changer une tuple en une liste
numero_list = list(numero)
print(numero_list)

# Ajouter un nouveau élément à l’index numéro 3
numero_list.insert(3, 707)

#Afficher une liste apres avoir insert un nouveau élément sur l’index numéro 3
print("-----Afficher une nouvelle liste apres avoir changer la tuple en une liste----\n")
for i in numero_list:
    print(i)

#Changer une liste en une tuple apres avoir insert un nouveau élément sur l’index numéro 3
numero_tuple = tuple(numero_list)

#Afficher une tuple apres avoir insert un nouveau élément sur l’index numéro 3
print("-----Afficher une nouvelle tuple apres avoir changer la liste en une tuple----\n")
for i in numero_tuple:
    print(i)

# 6. Afficher la nouvelle tuple
print("-----6. Afficher la nouvelle tuple-----\n")
  
nouvelle_tuple=numero_tuple
print(nouvelle_tuple)

print("--------------------------------------------------------------------------------------------------------------------------\n")

# III.Création d'un set qui contient 10 éléments

print("III.Creation d'un set qui contient 10 elements\n")

marque_ordinateur={"Fujistu","Acer","Asus","Dell","HP","Huawei","Lenovo","MSI","Razer","Apple"}

# 1. Afficher le set
print("----1. Affichage d'un set----\n")

for i in marque_ordinateur:
    print(i)

# 2.  Ajouter un élément
print("----2. Ajouter un element----\n")

# Ajouter un nouveau élément
marque_ordinateur.add("Toshiba")

# Affichage apres avoir ajout un élément
for i in marque_ordinateur:
    print(i)

# 3. Supprimer un élément
print("-----3. Supprimer un element-----\n")

# Suppression d'un élément
marque_ordinateur.remove("Razer")

# Affichage apres avoir supprimer un élément
for i in marque_ordinateur:
    print(i)

# 4. Supprimer le set
print("-----4. Supprimer le set-----\n")

# Suppression de set
del marque_ordinateur

print("--------------------------------------------------------------------------------------------------------------------------\n")

# IV.Création d'un dictionnaire qui contient 10 éléments

print("IV.Creation d'un dictionnaire qui contient 10 elements\n")

fichier_etudiant={"Nom":"Ngabirano", "Prenom":"Guy Michel", "Telephone":"+257868689", 
                  "Etat_Civil":"Celibataire", "Date_Naissance":"1/7/2000", "Lieu_Naissance":"Ngagara", 
                  "Domicilite":"Ngagara", "Travail":"Etudiant", "Faculte":"Inforamtique",
                  "Departement":"Genie Logiciel"}

# 1. Afficher le dictionnaire
print("----1. Afficher le dictionnaire----\n")

print(fichier_etudiant)

# 2. Afficher seulement les clés
print("-------2. Affichage des cles seulement-------\n")

for i in fichier_etudiant.keys():
    print(i)

# 3. Afficher seulement les valeurs
print("-------3. Affichage des valeurs seulement-------\n")

for i in fichier_etudiant.values():
    print(i)

# 4. Afficher les clés et les valeurs sous le format : Clé : Valeur
print("-------4. Affichage des cles et des valeurs sous le format : Cle : Valeur-------\n")

for i,j in fichier_etudiant.items():
    print(f"{i} : {j}")

# 5. Supprimer l'élément à la clé numéro 2
print("-----5. Supprimer l'element a la cle numero 2-----\n")

# Suppression d'élément qui se trouve à la clé numéro 2
key = "Prenom"
del fichier_etudiant[key]

# Affichage apres avoir supprimer l'élément qui se trouve à la clé numéro 2
print(fichier_etudiant)

# 6. Afficher l'élément de la clé numéro 5
print("-----6. Afficher l'element de la cle numero 5-----\n")

key = "Lieu_Naissance"
print(fichier_etudiant[key])

# 7.  Ajouter un nouvel élément
print("-------7. Ajouter un nouvel element-------\n")

# Ajout d'un nouvel élément
fichier_etudiant["Classe"] = "Bac3"
print(fichier_etudiant)

# 8. Créer une copie du dictionnaire
print("----8. Creer une copie du dictionnaire-----\n")

# Création d'une copie d'un dictionnaire
fichier_etudiant_copy = fichier_etudiant.copy()
print(fichier_etudiant_copy)