nom_fichier = input("Entrez le nom du fichier : ")
try:
    with open(nom_fichier, "r") as f:
        contenu = f.read()
        print("Contenu du fichier :")
        print(contenu)
except FileNotFoundError:
    print(f"Erreur : Le fichier '{nom_fichier}' n'existe pas.")
except Exception as e:
    print(f"Une erreur inattendue est survenue : {e}")