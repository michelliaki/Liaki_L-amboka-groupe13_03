role = input("Rôle (employé/visiteur/sécurité) : ").lower()

if role == "employé":
    badge = input("Badge valide (oui/non) : ").lower()
    if badge == "oui":
        print("Accès autorisé.")
    else:
        print("Accès refusé, badge invalide.")
elif role == "visiteur":
    rdv = input("Avez-vous un rendez-vous (oui/non) : ").lower()
    if rdv == "oui":
        print("Accès autorisé.")
    else:
        print("Accès refusé, pas de rendez-vous.")
elif role == "securite":
    print("Accès autorisé.")
else:
    print("Accès refusé, rôle inconnu.")