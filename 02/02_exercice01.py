#Demander deux nombres
a = float(input("Entrez le premier nombre: "))
b = float(input("Entrez le deuxième nombre: "))

#Calculs
somme = a + b
difference = a - b
produit = a * b

# Gérer la division par zéro
if b != 0:
    quotient = a / b
    division_entiere = a // b
    reste = a % b
else:
    quotient = "Division par zéro"
    division_entiere = "Division par zéro"
    reste = "Division par zéro"

#Affichage des résultats
print(f"Somme: {somme}")
print(f"Différence: {difference}")
print(f"Produit: {produit}")
print(f"Quotient: {quotient}")
print(f"Division entière: {division_entiere}")
print(f"Reste: {reste}")