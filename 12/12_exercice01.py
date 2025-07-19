noms_utilisateurs = []
while True:
    nom = input("Entrez un nom d'utilisateur ('stop' pour finir) : ")
    if nom.lower() == 'stop':
        break
    noms_utilisateurs.append(nom)

with open("utilisateurs.txt", "w") as f:
    for nom in noms_utilisateurs:
        f.write(nom + "\n")

print("Noms d'utilisateurs sauvegardés dans utilisateurs.txt")