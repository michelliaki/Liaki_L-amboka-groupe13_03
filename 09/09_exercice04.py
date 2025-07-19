phrase = input("Entrez une phrase ou un titre : ")
mots = phrase.split()

acronyme = ""
for mot in mots:
    if mot: # Pour éviter les mots vides si plusieurs espaces
        acronyme += mot[0].upper()

print(f"Acronyme : {acronyme}")