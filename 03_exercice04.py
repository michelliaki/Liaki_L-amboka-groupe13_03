temp = float(input("Température (°C): "))

if temp >= 35:
    print("Très chaud, restez hydraté.")
elif temp >= 25:
    print("Chaud, faites attention au soleil.")
elif temp >= 15:
    print("Température agréable.")
else:
    print("Il fait frais, couvrez-vous.")