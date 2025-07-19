age = int(input("Age : "))
statut = input("Statut (étudiant/salarié/retraité) : ").lower()

if age < 18:
    tarif = 5
else:
    if age <= 25:
        if statut == "etudiant":
            tarif = 6
        elif statut == "salarié":
            tarif = 8
        else:
            tarif = 10 # Pas étudiant ni salarié, mais jeune
    else:
        if statut == "retraité":
            tarif = 7
        else:
            tarif = 10

print(f"Le tarif est de {tarif} €")