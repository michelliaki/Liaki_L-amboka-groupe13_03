livres = [
    {"titre": "Python Débutant", "auteur": "Dupont", "année": 2018},
    {"titre": "Maîtriser Python", "auteur": "Martin", "année": 2021},
    {"titre": "Apprendre le Python", "auteur": "Durand", "année": 2020}
]

print("Livres publiés après 2010 :")
for livre in livres:
    if livre["année"] > 2010:
        print(f"Titre: {livre['titre']} ({livre['auteur']}) - {livre['année']}")