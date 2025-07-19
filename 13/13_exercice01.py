try:
    num1 = float(input("Entrez le premier nombre : "))
    num2 = float(input("Entrez le deuxième nombre : "))
    resultat = num1 / num2
    print(f"Le quotient est : {resultat}")
except ZeroDivisionError:
    print("Erreur : Division par zéro impossible.")
except ValueError:
    print("Erreur : Veuillez entrer des nombres valides.")