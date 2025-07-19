texte = input("Entrez un texte : ")

texte_nettoye = texte.strip().lower().replace(".", "!")

print(f"Texte nettoyé : {texte_nettoye}")