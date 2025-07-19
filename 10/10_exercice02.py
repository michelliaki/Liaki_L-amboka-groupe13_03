entree = input("Entrez une liste d'éléments séparés par des espaces : ")
liste = entree.split()

liste_inversee = liste[::-1]

print(f"Liste inversée : {liste_inversee}")