mots = input("Entrez une liste de mots séparés par des espaces : ").split()
voyelles = "aeiouAEIOU"
total_voyelles = 0

for mot in mots:
    for lettre in mot:
        if lettre in voyelles:
            total_voyelles += 1

print(f"Nombre total de voyelles : {total_voyelles}")