entree = input("Entrez des nombres séparés par des espaces : ")
liste = [int(x) for x in entree.split()]

n = len(liste)
for i in range(n - 1):
    for j in range(n - i - 1):
        if liste[j] > liste[j+1]:
            liste[j], liste[j+1] = liste[j+1], liste[j] # Échange

print(f"Liste triée : {liste}")