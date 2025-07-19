mot = input("Entrez un mot d'au moins 5 lettres : ")

if len(mot) >= 5:
    milieu = mot[2:-2]
    print(f"Partie centrale : {milieu}")
else:
    print("Le mot doit avoir au moins 5 lettres.")