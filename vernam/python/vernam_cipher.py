import random 
import string

text_input=input("Enter text ")

ciphers="0123456789"+string.ascii_lowercase+string.ascii_uppercase

def get_key(text_input):
    text_key=""
    for every in text_input:
        num=random.randint(0,len(ciphers))
        text_key +=ciphers[num]
    return text_key

def get_index(input_text):
    list_return=[]
    for every in input_text:
        list_return.append(ciphers.index(every))
    return list_return

def get_list(text):
    return [i for i in text]

text_list=get_list(text_input)
cipher_list=get_list(get_key(text_input))

print(text_list)
print(cipher_list)

index_message=get_index(text_list)
index_ciphertext=get_index(cipher_list)

print(index_message)

print(index_ciphertext)

answer_list=[]

def get_charachter(list_numbers):
    list_charachters=[]
    for i in list_numbers:
        list_charachters.append(ciphers[i])
    return list_charachters

for a in range(0,len(index_message)):
    answer_list.append(index_message[a]^index_ciphertext[a])
print(answer_list)

print(get_charachter(answer_list))

