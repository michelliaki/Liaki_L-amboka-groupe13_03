phrase = input("Entrez une phrase : ")

nombre_mots = len(phrase.split())
nombre_caracteres = len(phrase)

with open("rapport_analyse.txt", "w") as f:
    f.write("--- Rapport d'analyse de texte ---\n")
    f.write(f"Phrase : {phrase}\n")
    f.write(f"Nombre de mots : {nombre_mots}\n")
    f.write(f"Nombre de caractères : {nombre_caracteres}\n")

print("Rapport d'analyse sauvegardé dans rapport_analyse.txt")