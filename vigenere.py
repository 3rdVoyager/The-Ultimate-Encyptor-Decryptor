# This module implements the Vigenère cipher, which is a method of encrypting alphabetic text by using a simple form of polyalphabetic substitution. The module includes functions for getting the key from the user, encrypting and decrypting messages, and determining which function to call based on the user's choice of mode (encryption or decryption).
def get_key(cipher):
    if cipher.lower() == 'v':
        while True:
            key = input("Enter the keyword (a non-empty string): ").strip()
            if key.isalpha():
                return key
            else:                
                print("Invalid key. Please enter a non-empty string consisting of letters only.")

# The encrypt function takes a message and a key, and returns the encrypted message by applying the Vigenère cipher algorithm, which involves shifting each letter in the message by an amount determined by the corresponding letter in the key.
def encrypt(message, key):
    result = ""
    key = key * (len(message) // len(key)) + key[:len(message) % len(key)]
    for i in range(len(message)):
        char = message[i]
        if char.isupper():
            encrypted_char = chr((ord(char) + ord(key[i]) - 2 * ord('A')) % 26 + ord('A'))
        elif char.islower():
            encrypted_char = chr((ord(char) + ord(key[i]) - 2 * ord('a')) % 26 + ord('a'))
        else:
            encrypted_char = char
        result += encrypted_char
    return result

# The decrypt function takes an encrypted message and a key, and returns the decrypted message by applying the inverse of the Vigenère cipher algorithm, which involves shifting each letter in the encrypted message back by an amount determined by the corresponding letter in the key.
def decrypt(message, key):
    result = ""
    key = key * (len(message) // len(key)) + key[:len(message) % len(key)]
    for i in range(len(message)):
        char = message[i]
        if char.isupper():
            decrypted_char = chr((ord(char) - ord(key[i]) + 26) % 26 + ord('A'))
        elif char.islower():
            decrypted_char = chr((ord(char) - ord(key[i]) + 26) % 26 + ord('a'))
        else:
            decrypted_char = char
        result += decrypted_char
    return result

# The encrypt_decrypt function determines whether to call the encrypt or decrypt function based on the user's choice of mode (encryption or decryption).
def encrypt_decrypt(cipher, mode, message, key):
    if cipher == 'v':
        if mode == 'e':
            return encrypt(message, key)
        elif mode == 'd':
            return decrypt(message, key)