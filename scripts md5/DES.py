from Crypto.Cipher import DES
from secrets import token_bytes

def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

key = token_bytes(8)
cipher = DES.new(key, DES.MODE_ECB)

plaintext = "Bonjour le monde"
padded_text = pad(plaintext)
ciphertext = cipher.encrypt(padded_text.encode('utf-8'))
print(f"phrase a chiffré: {plaintext}")
print(f"Chiffré: {ciphertext}")

# Déchiffrement
decipher = DES.new(key, DES.MODE_ECB)
decrypted_text = decipher.decrypt(ciphertext).decode('utf-8').strip()
print(f"Déchiffré: {decrypted_text}")