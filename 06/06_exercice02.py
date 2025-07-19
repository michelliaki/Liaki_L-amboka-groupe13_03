choix = ""

while choix != "0":
    print("\n--- MENU ---")
    print("1. Dire bonjour")
    print("2. Additionner deux nombres")
    print("0. Quitter")

    choix = input("Votre choix : ")

    if choix == "1":
        print("Bonjour !")
    elif choix == "2":
        a = float(input("Entrez le premier nombre : "))
        b = float(input("Entrez le deuxième nombre : "))
        print(f"Le résultat est : {a + b}")
    elif choix == "0":
        print("Au revoir !")
    else:
        print("Choix invalide.")