texte = input("Entrez un texte : ")
mot_cherche = input("Entrez le mot à chercher : ")

# Convertir les deux en minuscules pour une recherche insensible à la casse
texte_lower = texte.lower()
mot_cherche_lower = mot_cherche.lower()

occurrences = texte_lower.count(mot_cherche_lower)

print(f"Le mot '{mot_cherche}' apparaît {occurrences} fois.")