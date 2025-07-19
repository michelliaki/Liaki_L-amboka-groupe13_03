import random
import string

def generer_mot_de_passe(longueur):
    caracteres = string.ascii_letters + string.digits
    mdp = ''.join(random.choice(caracteres) for i in range(longueur))
    return mdp

# Exemple d'utilisation
# longueur_mdp = int(input("Entrez la longueur du mot de passe souhaitée : "))
# mot_de_passe_genere = generer_mot_de_passe(longueur_mdp)
# print(f"Mot de passe généré : {mot_de_passe_genere}")