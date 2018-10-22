import binascii
import random
def toHex(word):
    return int(str(binascii.hexlify(word.encode()), 'ascii'), 16)
 
def toString(word):
    return str(binascii.unhexlify(hex(word)[2:]), 'ascii')

def encrypt(message, key):
    message = toHex(message)
    key = toHex(key)

    return message ^ key

def decrypt(code, key):
    key = toHex(key)
    return toString(code ^ key)

def main():
    msg = input("Hva er meldingen?")

    key = list(msg)
    random.shuffle(key)
    key = ''.join(key)


    crypt = encrypt(msg, key)
    msg = decrypt(crypt, key)
    print("Encrypted:", crypt)
    print("Decrypted", msg)

main()

