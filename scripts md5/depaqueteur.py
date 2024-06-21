import binascii

A='d131dd02c5e6eec4693d9a0698aff95c2fcab58712467eab4004583eb8fb7f8955ad340609f4b30283e488832571415a085125e8f7cdc99fd91dbdf280373c5bd8823e3156348f5bae6dacd436c919c6dd53e2b487da03fd02396306d248cda0e99f33420f577ee8ce54b67080a80d1ec69821bcb6a8839396f9652b6ff72a70'
B='d131dd02c5e6eec4693d9a0698aff95c2fcab50712467eab4004583eb8fb7f8955ad340609f4b30283e4888325f1415a085125e8f7cdc99fd91dbd7280373c5bd8823e3156348f5bae6dacd436c919c6dd53e23487da03fd02396306d248cda0e99f33420f577ee8ce54b67080280d1ec69821bcb6a8839396f965ab6ff72a70'

vect1=binascii.a2b_hex(A)
vect2=binascii.a2b_hex(B)

for i in range(len(vect1)):
       if(vect1[i]!=vect2[i]):
            print("vect1[%d]=0x%x, vect2[%d]=0x%x" %(i, vect1[i], i, vect2[i]))

import sys
TailleVect=128
TailleHelloWorld=29220
TailleMalware=29220

binaire=open(sys.argv[1],'rb').read()
output=open('output.exe', 'wb')

if binaire[19]==0X87:
    #extraction de HelloWorld.exe
    output.write(binaire[TailleVect:TailleVect+TailleHelloWorld])
else:
    #extraction de Malware.exe
    output.write(binaire[TailleVect+TailleHelloWorld:TailleVect+TailleHelloWorld+TailleMalware])

output.close()