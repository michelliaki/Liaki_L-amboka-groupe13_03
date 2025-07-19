plat = input("Quel type de plat voulez-vous (viande, poisson, végétarien) : ").lower()

if plat == "viande":
    cuisson = input("Cuisson (saignant, à point, bien cuit) : ").lower()
    print(f"Vous avez choisi de la viande {cuisson}.")
elif plat == "poisson":
    sauce = input("Sauce (citron, beurre) : ").lower()
    print(f"Vous avez choisi du poisson avec sauce {sauce}.")
elif plat == "vegetarien":
    choix = input("Souhaitez-vous salade ou pâtes ? ").lower()
    print(f"Vous avez choisi {choix}.")
else:
    print("Choix invalide.")