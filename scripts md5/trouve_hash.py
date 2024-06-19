import hashlib

def obtenir_hash_md5():
    # Demander à l'utilisateur de saisir un mot ou une phrase
    texte = input("Entrez un mot ou une phrase : ")

    # Convertir le texte en bytes
    texte_bytes = texte.encode('utf-8')

    # Calculer le hachage MD5
    hash_md5 = hashlib.md5(texte_bytes).hexdigest()

    # Afficher le hachage MD5
    print(f"Le hachage MD5 est : {hash_md5}")

# Appeler la fonction pour exécuter le script
obtenir_hash_md5()
