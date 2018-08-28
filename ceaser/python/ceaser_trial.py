def encrypt(string, shift):
    result = ""
    for i in string:
        if(i.isupper()):
            result += chr((ord(i) + shift))
        else:
            result += chr((ord(i) + shift))
    return result

def decrypt(string, shift):
    result = ""
    for i in string:
        if(i.isupper()):
            result += chr((ord(i) - shift))
        else:
            result += chr((ord(i) - shift))
    return result


encrypted=encrypt("Hello World",4)
print(encrypted)

print(decrypt(encrypted,4))