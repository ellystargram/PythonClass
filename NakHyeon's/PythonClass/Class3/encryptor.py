ascii_min = 32
ascii_max = 126

key = 314159
key = str(key)


def encrypt(message):
    encrypted_message = ""
    for index in range(len(message)):
        char = ord(message[index])
        if char < ascii_min or char > ascii_max:
            encrypted_message += message[index]
        else:
            asc_num = char + int(key[index % len(key)])
            if asc_num > ascii_max:
                asc_num -= ascii_max - ascii_min + 1
            encrypted_message += chr(asc_num)
    return encrypted_message


def decrypt(message):
    decrypted_message = ""
    for index in range(len(message)):
        char = ord(message[index])
        if char < ascii_min or char > ascii_max:
            decrypted_message += message[index]
        else:
            asc_num = char - int(key[index % len(key)])
            if asc_num < ascii_min:
                asc_num += ascii_max - ascii_min + 1
            decrypted_message += chr(asc_num)
    return decrypted_message


in_put = input("Enter the message to encrypt: ")
output = encrypt(in_put)

print("Encrypted message: ", output)

output = "Fphjsp#jw!hxrm%"

output = decrypt(output)

print("Decrypted message: ", output)

import toolkit

output = toolkit.quantomize(in_put)
print("Quantomized message: ", output)

output = toolkit.dequantomize(output)
print("Dequantomized message: ", output)
