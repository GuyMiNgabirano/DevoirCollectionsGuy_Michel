if __name__ == "__main__":

   #Création d'une liste qui contient 10 éléments 

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