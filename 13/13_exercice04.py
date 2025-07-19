while True:
    try:
        entier_positif = int(input("Entrez un entier positif : "))
        if entier_positif > 0:
            print(f"Vous avez saisi : {entier_positif}")
            break
        else:
            print("Veuillez entrer un nombre positif.")
    except ValueError:
        print("Saisie invalide. Veuillez entrer un nombre entier.")