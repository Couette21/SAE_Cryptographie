import binascii
import hashlib

# Chaînes hexadécimales A et B
A = 'd131dd02c5e6eec4693d9a0698aff95c2fcab58712467eab4004583eb8fb7f8955ad340609f4b30283e488832571415a085125e8f7cdc99fd91dbdf280373c5bd8823e3156348f5bae6dacd436c919c6dd53e2b487da03fd02396306d248cda0e99f33420f577ee8ce54b67080a80d1ec69821bcb6a8839396f9652b6ff72a70'
B = 'd131dd02c5e6eec4693d9a0698aff95c2fcab50712467eab4004583eb8fb7f8955ad340609f4b30283e4888325f1415a085125e8f7cdc99fd91dbd7280373c5bd8823e3156348f5bae6dacd436c919c6dd53e23487da03fd02396306d248cda0e99f33420f577ee8ce54b67080280d1ec69821bcb6a8839396f965ab6ff72a70'

# Conversion des chaînes hexadécimales en données binaires
vect1 = binascii.a2b_hex(A)
vect2 = binascii.a2b_hex(B)

# Calcul du hash MD5 pour vect1 et vect2
hash1 = hashlib.md5(vect1).hexdigest()
hash2 = hashlib.md5(vect2).hexdigest()

# Affichage des résultats
print(f"Hash MD5 de vect1 : {hash1}")
print(f"Hash MD5 de vect2 : {hash2}")
