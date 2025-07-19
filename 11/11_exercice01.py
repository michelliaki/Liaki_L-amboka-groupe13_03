def calculer(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b != 0:
            return a / b
        else:
            return "Erreur : division par zéro"
    else:
        return "Opération non valide"

# Exemple d'utilisation
# num1 = float(input("Entrez le premier nombre : "))
# num2 = float(input("Entrez le deuxième nombre : "))
# operation = input("Entrez l'opération (+, -, *, /) : ")
#
# resultat = calculer(num1, num2, operation)
# print(f"Résultat : {resultat}")