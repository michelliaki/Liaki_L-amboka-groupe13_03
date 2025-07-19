import math

try:
    nombre = float(input("Entrez un nombre : "))
    if nombre >= 0:
        racine = math.sqrt(nombre)
        print(f"La racine carrée de {nombre} est {racine:.2f}")
    else:
        print("Impossible de calculer la racine carrée d'un nombre négatif.")
except ValueError:
    print("Saisie invalide. Veuillez entrer un nombre.")
finally:
    print("Fin de l'opération de calcul de racine carrée.")