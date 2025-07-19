carres = []

for i in range(1, 21):
    carres.append(i ** 2)

print(f"Liste des carrés : {carres}")

print("Carrés supérieurs à 100 :")
for val in carres:
    if val > 100:
        print(val)