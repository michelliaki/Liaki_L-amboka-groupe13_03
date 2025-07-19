note = float(input("Entrez votre note sur 100: "))

if note >= 90:
    print("Mention: Excellent")
elif note >= 75:
    print("Mention: Très Bien")
elif note >= 60:
    print("Mention: Bien")
elif note >= 50:
    print("Mention: Passable")
else:
    print("Mention: Insuffisant")