#when transferring key from wifi the key gets encryted good for cybersecurity
import string#instaed of writing long words or letters use this
import random

chars=' '+ string.punctuation + string.digits + string.ascii_letters
#this means  every puntuation and digits and every letter both in a lower or upper case
#NOTE if i wanted to add a space i can put in string.whitespace but this give an entire line of free space instead u add ' '
chars= list(chars) #this turns strings and turn them into a list
key= chars.copy()#this copys the input and gives it to key
#lets shuffle this key
random.shuffle(key)
# print(f'Chars: {chars}')
# print (f'Key: {key}')
#Encrytion
plain_text=input('Password key: ')
cipher_text=''
for letter in plain_text:
    index=chars.index(letter)#this finds the position of the letter in the chars list
    cipher_text+= key[index]

print(f'Encrypted message: {cipher_text}')
#Decryption
cipher_text=input('Encryted key: ')
plain_text=''
for letter in cipher_text:
    index=key.index(letter)#this finds the position of the letter in the chars list
    plain_text+= chars[index]

print(f'Decrypted message: {plain_text}')
