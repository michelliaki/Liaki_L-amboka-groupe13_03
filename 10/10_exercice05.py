entree = input("Entrez une liste de nombres séparés par des espaces : ")
nombres = [int(x) for x in entree.split()]

elements_pairs = nombres[::2]

print(f"Éléments aux indices pairs : {elements_pairs}")