texte = input("Entrez un texte : ")
try:
    entier = int(texte)
    print(f"Le texte a été converti en entier : {entier}")
except ValueError:
    print("Erreur : Impossible de convertir le texte en entier.")