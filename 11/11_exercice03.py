def est_palindrome(mot):
    mot_inverse = mot[::-1]
    return mot.lower() == mot_inverse.lower()

# Exemple d'utilisation
# mot_test = input("Entrez un mot : ")
# if est_palindrome(mot_test):
#     print(f"'{mot_test}' est un palindrome.")
# else:
#     print(f"'{mot_test}' n'est pas un palindrome.")