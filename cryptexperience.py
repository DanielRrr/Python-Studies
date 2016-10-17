import simplecrypt

with open("passwords.txt", "rb") as inp:
    passwords = inp.read().decode('utf-8').split("\n")
    with open("encrypted.bin", "rb") as encr:
        infotext = encr.read()
        for password in passwords:
            try:
                plaintext = simplecrypt.decrypt(password, infotext)
            except:
                pass
            else:
                print(plaintext.decode('utf-8'))
