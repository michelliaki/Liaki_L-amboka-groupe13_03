n = int(input("Entrez un entier positif : "))

if n < 0:
    print("Veuillez entrer un nombre positif.")
else:
    fact = 1
    i = 1
    while i <= n:
        fact *= i
        i += 1
    print(f"La factorielle de {n} est {fact}")