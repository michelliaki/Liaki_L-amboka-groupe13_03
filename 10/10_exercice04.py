numero_tel = input("Entrez un numéro de téléphone (ex. 0897654321) : ")

if len(numero_tel) >= 3:
    masque = "*" * (len(numero_tel) - 3)
    numero_masque = masque + numero_tel[-3:]
    print(f"Numéro masqué : {numero_masque}")
else:
    print("Le numéro est trop court pour être masqué.")