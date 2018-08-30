import random 
import string

text_input=input("Enter text ")

ciphers="0123456789"+string.ascii_lowercase+string.ascii_uppercase
print(len(ciphers))
def get_key(text_input):
    text_key=""
    for every in text_input:
        num=random.randint( 0 , len(ciphers) - 1 ) 
        text_key += ciphers[num]
    print("generated key is ")
    print(text_key)
    return text_key

def get_index(input_text):
    list_return=[]
    for every in input_text:
        list_return.append(ciphers.index(every))
    return list_return

def get_charachter(list_numbers):
    list_charachters=[]
    for i in list_numbers:
        list_charachters.append(ciphers[i])
    return list_charachters


def create_vernam_cipher_clone(index_message,index_ciphertext):
    answer_list=[]
    for a in range(0,len(index_message)):
        answer_list.append(index_message[a]^index_ciphertext[a])
    return answer_list


def vernam_cipher_master(text_input,key_generated):
    list_index_text = get_index(text_input)
    list_index_key = get_index(key_generated)

    print("list of numbers of text is ")
    print(list_index_text)

    print("list of numbers of key is ")
    print(list_index_key)

    encrypted = create_vernam_cipher_clone(list_index_text,list_index_key)
    print("raw encrypted is ")
    print(encrypted)
    print("cipher text is ")
    print(get_charachter( encrypted))

    decrypted = create_vernam_cipher_clone(encrypted,list_index_key)
    print("raw Decrypted is ")
    print(decrypted)
    print("Decrypted is ")
    print(get_charachter(decrypted))


vernam_cipher_master(text_input,get_key(text_input))
