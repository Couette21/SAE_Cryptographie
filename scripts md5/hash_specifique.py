import os
import hashlib
import tkinter as tk
from tkinter import messagebox

# Nom du fichier
nom_fichier = "virtualbox-7.0_7.0.18-162988~Ubuntu~noble_amd64.deb"
# Chemin de destination
chemin_destination = "/home/theo/Bureau/scripts_md5/"

# Contenu initial du fichier
contenu_fichier = b"tu t fait avoir"

# Fonction pour afficher une pop-up (cross-platform)
def afficher_popup():
    racine = tk.Tk()
    racine.withdraw()
    messagebox.showinfo("Message", "tu t fait avoir")
    racine.destroy()

# Écrire le contenu initial dans le fichier
with open(nom_fichier, "wb") as fichier:
    fichier.write(contenu_fichier)

# Calculer le hash MD5 du fichier
def calculer_md5(chemin_fichier):
    hash_md5 = hashlib.md5()
    with open(chemin_fichier, "rb") as fichier:
        for morceau in iter(lambda: fichier.read(4096), b""):
            hash_md5.update(morceau)
    return hash_md5.hexdigest()

# Ajuster le fichier pour obtenir le hash MD5 souhaité
md5_cible = "fa778ac616585596a51dace9ddac2c5a"
md5_actuel = calculer_md5(nom_fichier)

while md5_actuel != md5_cible:
    with open(nom_fichier, "ab") as fichier:
        fichier.write(b"\0")
    md5_actuel = calculer_md5(nom_fichier)

print(f"Fichier créé avec le hash MD5 : {md5_actuel}")

# Déplacer le fichier vers le répertoire de destination
os.replace(nom_fichier, os.path.join(chemin_destination, nom_fichier))

# Afficher la pop-up
afficher_popup()

# Message de confirmation
print("Le fichier a été téléchargé.")
