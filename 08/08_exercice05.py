texte = input("Entrez un texte : ")
voyelles = "aeiouAEIOU"

for char in texte:
    if char.isalpha() and char not in voyelles:
        print(char, end="")
print() # Pour une nouvelle ligne à la fin