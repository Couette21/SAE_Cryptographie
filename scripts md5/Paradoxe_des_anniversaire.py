import hashlib
import random
import string

def generate_random_string(length=10):
    """Génère une chaîne aléatoire de la longueur spécifiée."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def md5_hash(text):
    """Calcule l'empreinte MD5 de la chaîne spécifiée."""
    return hashlib.md5(text.encode('utf-8')).hexdigest()

def find_collision(num_strings=10000):
    """Cherche des collisions MD5 parmi les chaînes aléatoires générées."""
    hashes = {}
    for _ in range(num_strings):
        random_string = generate_random_string()
        hash_value = md5_hash(random_string)
        if hash_value in hashes:
            return random_string, hashes[hash_value], hash_value
        hashes[hash_value] = random_string
    return None, None, None

if __name__ == "__main__":
    # Nombre de chaînes à générer
    num_strings = 100000

    str1, str2, hash_value = find_collision(num_strings)

    if str1 and str2:
        print(f"Collision trouvée après {num_strings} essais:")
        print(f"Chaîne 1: {str1}")
        print(f"Chaîne 2: {str2}")
        print(f"Empreinte MD5: {hash_value}")
    else:
        print(f"Aucune collision trouvée après {num_strings} essais.")