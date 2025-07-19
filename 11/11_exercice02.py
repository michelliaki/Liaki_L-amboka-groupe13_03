def generer_statistiques(liste_nombres):
    somme = sum(liste_nombres)
    moyenne = somme / len(liste_nombres) if liste_nombres else 0
    maximum = max(liste_nombres) if liste_nombres else None
    return somme, moyenne, maximum

# Exemple d'utilisation
# notes = [12, 15, 10, 18, 7]
# somme_notes, moyenne_notes, max_notes = generer_statistiques(notes)
# print(f"Somme : {somme_notes}")
# print(f"Moyenne : {moyenne_notes:.2f}")
# print(f"Maximum : {max_notes}")