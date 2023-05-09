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