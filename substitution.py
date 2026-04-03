# This module implements the substitution cipher, which is a type of encryption where each letter in the plaintext is replaced with a corresponding letter from a fixed substitution alphabet. The module includes functions for getting the key from the user, encrypting and decrypting messages, and determining which function to call based on the user's choice of mode (encryption or decryption).
import string
alphabet = string.ascii_lowercase

# The get_key function prompts the user to enter a key for the substitution cipher, which must be a 26-letter string with no repeated characters. It includes error handling to ensure that the user inputs a valid key.
def get_key(cipher):
    if cipher.lower() == 's':
        while True:
            key = input("Enter a 26-letter substitution key (no repeats): ").strip().lower()
            
            if len(key) == 26 and key.isalpha() and len(set(key)) == 26:
                return key
            else:
                print("Invalid key. Must be 26 unique letters.")

# The encrypt function takes a message and a key, and returns the encrypted message by replacing each letter in the message with the corresponding letter from the key.
def encrypt(message, key):
    result = ""
    for char in message:
        if char.lower() in alphabet:
            index = alphabet.index(char.lower())
            new_char = key[index]
            
            # preserve uppercase
            if char.isupper():
                result += new_char.upper()
            else:
                result += new_char
        else:
            result += char
    return result

# The decrypt function takes an encrypted message and a key, and returns the decrypted message by replacing each letter in the message with the corresponding letter from the alphabet based on the position of the letter in the key.
def decrypt(message, key):
    result = ""
    for char in message:
        if char.lower() in alphabet:
            index = key.index(char.lower())
            new_char = alphabet[index]
            
            if char.isupper():
                result += new_char.upper()
            else:
                result += new_char
        else:
            result += char
    return result

# The encrypt_decrypt function determines whether to call the encrypt or decrypt function based on the user's choice of mode (encryption or decryption).
def encrypt_decrypt(cipher, mode, message, key):
    if cipher == 's':
        if mode == 'e':
            return encrypt(message, key)
        elif mode == 'd':
            return decrypt(message, key)