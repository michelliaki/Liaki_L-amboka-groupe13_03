nombre = int(input("Entrez un nombre pour sa table de multiplication : "))

with open(f"table_de_{nombre}.txt", "w") as f:
    f.write(f"Table de multiplication de {nombre}:\n")
    for i in range(1, 13):
        f.write(f"{nombre} x {i} = {nombre * i}\n")

print(f"Table de multiplication sauvegardée dans table_de_{nombre}.txt")