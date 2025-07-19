phrase = input("Entrez une phrase : ")
mots = phrase.split()

mots_un_sur_deux = mots[::2]

print(f"Mots un sur deux : {mots_un_sur_deux}")