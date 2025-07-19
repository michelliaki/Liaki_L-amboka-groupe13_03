activite = input("Entrez une activité à ajouter au journal : ")

with open("journal_activites.txt", "a") as f:
    f.write(activite + "\n")

print("Activité ajoutée au journal.")