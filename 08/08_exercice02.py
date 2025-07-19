entree = input("Entrez des éléments séparés par des espaces : ")
liste = entree.split()

for i, elem in enumerate(liste):
    print(f"Indice {i} : {elem}")