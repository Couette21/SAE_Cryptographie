import hashlib
import os
import struct
import tkinter as tk
from tkinter import messagebox

# Nom du fichier
file_name = "virtualbox-7.0_7.0.18-162988~Ubuntu~noble_amd64.deb"
# Chemin de destination
destination_path = "/home/theo/Téléchargements/"

# Contenu initial du fichier
file_content = b"tu t fait avoir"

# Fonction pour afficher une pop-up (cross-platform)
def show_popup():
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Message", "tu t fait avoir")
    root.destroy()

# Écrire le contenu initial dans le fichier
with open(file_name, "wb") as f:
    f.write(file_content)

# Calculer le hash MD5 du fichier
def calculate_md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# Ajuster le fichier pour obtenir le hash MD5 souhaité
target_md5 = "fa778ac616585596a51dace9ddac2c5a"
current_md5 = calculate_md5(file_name)

while current_md5 != target_md5:
    with open(file_name, "ab") as f:
        f.write(b"\0")
    current_md5 = calculate_md5(file_name)

print(f"Fichier créé avec le hash MD5 : {current_md5}")
# Déplacer le fichier vers le répertoire de destination
os.replace(file_name, os.path.join(destination_path, file_name))
show_popup()
print("Le fichier a été téléchargé.")

