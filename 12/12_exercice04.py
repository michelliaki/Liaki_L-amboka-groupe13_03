entree_notes = input("Entrez une liste de notes séparées par des espaces : ")
notes = [float(x) for x in entree_notes.split()]

if notes:
    moyenne = sum(notes) / len(notes)
    with open("statistiques_notes.txt", "w") as f:
        f.write(f"Notes : {notes}\n")
        f.write(f"Moyenne : {moyenne:.2f}\n")
    print("Statistiques sauvegardées dans statistiques_notes.txt")
else:
    print("Aucune note saisie.")