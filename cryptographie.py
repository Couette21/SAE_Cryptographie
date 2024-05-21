import hashlib

# Fonction pour calculer le hachage MD5
def calculer_md5(texte):
    return hashlib.md5(texte.encode()).hexdigest()

# Exemple de deux textes différents
texte1 = "blabla"
texte2 = "blabla"

# Calcul des hachages
hachage1 = calculer_md5(texte1)
hachage2 = calculer_md5(texte2)

# Affichage des résultats
print(f"Texte 1 : {texte1}")
print(f"Hachage MD5 1 : {hachage1}")
print(f"Texte 2 : {texte2}")
print(f"Hachage MD5 2 : {hachage2}")

# Vérification de collision
if hachage1 == hachage2:
    print("Collision trouvée!")
else:
    print("Pas de collision.")
