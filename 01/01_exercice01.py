# Demande d'information à l'utilisateur

prenom = input("entrez votre prénom : ")
age = int(input(" Entrez votre âge :"))
ville = input(" Entrez votre ville :")
metier = input(" Entrez votre métier : ")

#Approximation des jours vécus

jours_vecus = age * 365

# Affichage formaté

print("\n=== PROFIL UTILISATEUR ===")
print(f"Prénom : {prenom}")
print(f"Âge : {age} ans ({jours_vecus} jours vécus environ)")
print(f"Ville : {ville}")
print(f"Métier : {metier}")

