#!/bin/bash

# Compilation des fichiers C
gcc -Wall -pedantic HelloWorld.c -o HelloWorld.exe
gcc -Wall -pedantic Malware.c -o Malware.exe

# Calcul des sommes de hachage MD5 et SHA1
echo "Hachages pour HelloWorld.exe:"
md5sum HelloWorld.exe
sha1sum HelloWorld.exe

echo "Hachages pour Malware.exe:"
md5sum Malware.exe
sha1sum Malware.exe
