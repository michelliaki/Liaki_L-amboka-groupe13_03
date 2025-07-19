fievre = input("Avez-vous de la fièvre ? (oui/non) : ").lower()

if fievre == "oui":
    douleurs = input("Avez-vous des douleurs ? (oui/non) : ").lower()
    if douleurs == "oui":
        print("Consulter un médecin.")
    else:
        print("Surveillez vos symptômes.")
else:
    toux = input("Avez-vous de la toux ? (oui/non) : ").lower()
    if toux == "oui":
        print("Repos conseillé.")
    else:
        print("Bonne santé.")