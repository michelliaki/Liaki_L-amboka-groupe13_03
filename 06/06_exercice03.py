somme = 0
nb_notes = 0

while True:
    note = float(input("Entrez une note (-1 pour arrêter) : "))
    if note == -1:
        break
    somme += note
    nb_notes += 1

if nb_notes > 0:
    moyenne = somme / nb_notes
    print(f"Moyenne des notes : {moyenne:.2f}")
else:
    print("Aucune note saisie.")