def encrypt(string, shift):
    result = ""
    for i in string:
        if(i.isupper()):
            result += chr((ord(i) + shift - 65) % 26 + 65)
        else:
            result += chr((ord(i) + shift - 97) % 26 + 97)
    return result

def decrypt(string, shift):
    result = ""
    for i in string:
        if(i.isupper()):
            result += chr((ord(i) - shift - 65) % 26 + 65)
        else:
            result += chr((ord(i) - shift - 97) % 26 + 97)
    return result

#word=input("Enter a word you want to be encrypted ")

encryptedText = encrypt("HelloWorld",4)
decryptedText = decrypt(encryptedText, 4)
print("Encrypted Text : ", encryptedText)
print("Decrypted Text : ", decryptedText)
