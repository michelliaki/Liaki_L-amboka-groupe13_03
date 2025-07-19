anciennete = int(input("Nombre d'ancienneté (années) : "))
note = int(input("Note de performance (1 à 5) : "))

if anciennete >= 5:
    if note >= 4:
        prime = 2000
    else:
        prime = 1000
else:
    if note >= 4:
        prime = 500
    else:
        prime = 0

print(f"Prime allouée : {prime} €")