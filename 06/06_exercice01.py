import random

# Générer un nombre aléatoire
nombre_secret = random.randint(1, 100)
essai = None

while essai != nombre_secret:
    essai = int(input("Devinez le nombre (entre 1 et 100) : "))
    if essai < nombre_secret:
        print("Trop petit !")
    elif essai > nombre_secret:
        print("Trop grand !")
else:
    print(f"Bravo ! Le nombre était {nombre_secret}")