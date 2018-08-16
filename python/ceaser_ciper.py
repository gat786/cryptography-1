def encrypt(string, shift):
    result = ""
    for i in string:
        if(i.isupper()):
            result += chr((ord(i) + shift - 65) % 26 + 65)
        else:
            result += chr((ord(i) + shift - 97) % 26 + 97)
    return result

print(encrypt("HelloWorld",4))

def decrypt(string, shift):
    result = ""
    for i in string:
        if(i.isupper()):
            result += chr((ord(i) - shift - 65) % 26 + 65)
        else:
            result += chr((ord(i) - shift - 97) % 26 + 97)
    return result

print(decrypt(encrypt("HelloWorld",4),4))
