entree = input("Entrez des nombres séparés par des espaces : ")
liste = [int(x) for x in entree.split()]

somme_pairs = 0

for nombre in liste:
    if nombre % 2 == 0:
        somme_pairs += nombre

print(f"Somme des nombres pairs : {somme_pairs}")