nombre = int(input("Entrez un nombre pour sa table de multiplication : "))

print(f"=== Table de {nombre} ===")
for i in range(1, 13):
    resultat = nombre * i
    print(f"{nombre} x {i} = {resultat}")