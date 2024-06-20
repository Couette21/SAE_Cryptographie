#!/bin/bash

# Créer un fichier avec les hashes à craquer
echo "5f4dcc3b5aa765d61d8327deb882cf99" > hashes.txt  # "password" en MD5

# Utiliser hashcat pour craquer le mot de passe
hashcat -m 0 -a 0 hashes.txt /usr/share/wordlists/rockyou.txt

# chmod +x crack_password.sh
