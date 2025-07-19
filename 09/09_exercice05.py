phrase = input("Entrez une phrase : ")
mot_a_masquer = input("Entrez le mot à masquer : ")

masque = "*" * len(mot_a_masquer)
phrase_masquee = phrase.replace(mot_a_masquer, masque)

print(f"Phrase masquée : {phrase_masquee}")