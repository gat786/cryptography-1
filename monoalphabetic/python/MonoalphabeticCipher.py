listAlphabets=[ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

listCipherText=['J', 'R', 'C', 'Q', 'G', 'T', 'N', 'D',
                 'E', 'A', 'M', 'S', 'I', 'F', 'V', 'B',
                  'H', 'Z', 'X', 'P', 'W', 'L', 'Y', 'K', 'U', 'O']

inputString=input("Enter Text ")

def getEncrypted(inputString):
    generatedText=""
    for value in inputString:
        generatedText += listCipherText[listAlphabets.index(value)]
    return generatedText


def getDecrypted(inputString):
    generatedText=""
    for value in inputString:
        generatedText += listAlphabets[listCipherText.index(value)]
    return generatedText
encrypted=getEncrypted(inputString)
print(encrypted)
print(getDecrypted(encrypted))