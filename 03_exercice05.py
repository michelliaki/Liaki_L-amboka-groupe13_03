mdp = input("Entrez un mot de passe: ")

if len(mdp) >= 8 and any(c.isdigit() for c in mdp) and any(c.isupper() for c in mdp):
    print("Mot de passe valide.")
else:
    print("Mot de passe invalide.")