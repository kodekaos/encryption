# -*- coding: utf8 -*- 

import hashlib
import os

testline = '?!?'

def encrypt_file(key, in_file, out_file=None):
    if not out_file:
        out_file = in_file + '.enc'
    h = hashlib.md5(key)                                    # Lager en hash av key
    passkey = int(str(int(h.hexdigest(), 16))[::10])        
            # int(h.hexdigest(), 16) gjør om hex-verdien av h til en integer. 
            # str()[::10] konverterer integer til string og plukker ut hvert 10 element
            # int() konverterer tilbake til integer
    check_phrase = [(ord(c) + passkey) for c in testline]   
            # gjør om hver karakter i testline til en int med (ord(c),
            # legger deretter til passkey, for å få en unik linje for denne nøkkelen

    with open(in_file, 'r') as infile:
        with open (out_file, 'w') as outfile:
            outfile.writelines(''.join(map(str,check_phrase))+'\n')
                # map(str,chekc_phrase) gjør om karakterene i check_phrase til string.
                # ''.join()+\n slår sammen karakterene i strengen til en linje uten mellomrom
                # Dette for å ha en unik linje for nøkkelen i begynnelsen av fila
            for line in infile.readlines():
                content = [(ord(c) + passkey) for c in line]
                    # ord(c) konverterer hver karakter på linja til ASCII-verdi, legg deretter til passkey.
                outfile.writelines('$$'.join(map(str, content))+'\n')
                    # map(str, content) gjør om hver integer i innholdslista til en string
                    # '$$'.join()+\n skriver hver karakter til fila med $$ mellom seg
        print 'Encrypting content in', ''.join(os.path.splitext(in_file))
        print 'Output sent to', ''.join(os.path.splitext(out_file))

            
def decrypt_file(key, in_file, out_file=None):            
    if not out_file:
        out_file= os.path.splitext(in_file)[0]

    h = hashlib.md5(key)
    passkey = int(str(int(h.hexdigest(), 16))[::10])
    check_phrase = [(ord(c) + passkey) for c in testline]

    with open(in_file, 'r') as infile:
        check = (''.join(map(str,check_phrase))+'\n')
            # lager nøkkel som i encrypt, basert på ny hash
        if check == infile.readline():
                # Sjekker om ny passkey matcher det som står i første linje i fila
            with open(out_file, 'w') as outfile:
                for line in infile.readlines():
                    ascii = []
                    ordinal = [(int(d) - passkey) for d in line.split('$$')]
                        # henter ut krypterte karakterer mellom $$, gjør om til integer og tar bort passkey.
                        # Hver ordinal blir et element i en liste
                    for c in ordinal:
                        ascii.append(chr(c))
                            # konverterer hver ordinal tilbake til karakter og legger det til i en ny liste
                    outfile.writelines(''.join(ascii))
                        # Slår sammen hver karakter i ascii-listen uten mellomrom
            print 'Successfylly decrypted', ''.join(os.path.splitext(in_file))
            print 'Output sent to', ''.join(os.path.splitext(out_file))
            return True

        else:
            print 'invalid key'
            return False