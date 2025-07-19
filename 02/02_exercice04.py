note1 = float(input("Première note: "))
note2 = float(input("Deuxième note: "))
note3 = float(input("Troisième note: "))

moyenne = (note1 + note2 + note3) / 3

print(f"Moyenne: {moyenne:.2f}")

if moyenne >= 10:
    print("L'étudiant est reçu.")
else:
    print("L'étudiant n'est pas reçu.")