montant_ht = float(input("Montant HT (€): "))
taux_tva = float(input("Taux de TVA (%):"))

# Conversion en coefficient multiplicateur
taux_coef = taux_tva / 100

# Calcul TTC
montant_ttc = montant_ht * (1 + taux_coef)

print(f"Montant TTC: {montant_ttc:.2f} €")