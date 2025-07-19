etudiants = [("Alice", 18), ("Bob", 14), ("Charlie", 16), ("David", 12)]

print("Étudiants avec note >= 15 :")
for nom, note in etudiants:
    if note >= 15:
        print(f"Nom : {nom}")