def convertir_devises(montant_usd):
    eur = montant_usd * 0.93
    cfa = montant_usd * 610
    gbp = montant_usd * 0.79
    return eur, cfa, gbp

# Exemple d'utilisation
# montant = float(input("Entrez le montant en USD : "))
# euros, francs_cfa, livres_sterling = convertir_devises(montant)
# print(f"{montant} USD = {euros:.2f} EUR")
# print(f"{montant} USD = {francs_cfa:.2f} CFA")
# print(f"{montant} USD = {livres_sterling:.2f} GBP")