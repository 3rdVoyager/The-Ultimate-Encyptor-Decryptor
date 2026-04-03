# This module implements the Caesar cipher, which is a simple substitution cipher that shifts each letter in the plaintext by a fixed number of positions down the alphabet. The module includes functions for getting the key from the user, encrypting and decrypting messages, determining which function to call based on the user's choice of mode (encryption or decryption), and an experimental function for force decrypting messages without knowing the key.


# The get_key function prompts the user to enter a key for the Caesar cipher, which must be a number between 1 and 25. It includes error handling to ensure that the user inputs a valid key.
def get_key(cipher):
    if cipher.lower() == 'c':
        while True:
            key = input("Enter the key (a number between 1 and 25): ")
            if key.isdigit() and 1 <= int(key) <= 25:
                return int(key)
            else:
                print("Invalid key. Please enter a number between 1 and 25.")

# The encrypt function takes a message and a key, and returns the encrypted message by shifting each letter in the message by the specified number of positions. 
def encrypt(message, key):
    result = ""
    # Loop through each character in the input message
    for char in message:
        # Check if the character is an alphabetic character
        if char.isalpha():
            base = ord("a") if char.islower() else ord("A")                
            result += chr((ord(char) - base + key) % 26 + base)
        else:
            result += char
    return result

# The decrypt function takes an encrypted message and a key, and returns the decrypted message by shifting each letter back by the specified number of positions.
def decrypt(message, key):
    result = ""
    # Loop through each character in the input message
    for char in message:
        # Check if the character is an alphabetic character
        if char.isalpha():
            base = ord("a") if char.islower() else ord("A")
            result += chr((ord(char) - base - key) % 26 + base)
        # If the character is not alphabetic, add it to the result without changing it
        else:
            result += char
    return result

# The encrypt_decrypt function determines whether to call the encrypt or decrypt function based on the user's choice of mode (encryption or decryption). 
def encrypt_decrypt(cipher, mode, message, key):
    if cipher == 'c':
        if mode == 'e':
            return encrypt(message, key)
        elif mode == 'd':
            return decrypt(message, key)



# The following functions are for force decrypting a message encrypted with the Caesar cipher without knowing the key, by trying all possible keys and checking for plausibility of the decrypted messages. This is an experimental feature that is undergoing development.
"""
def force_decrypt(result):
    found = False
    print("Attempting to force decrypt the message with all possible keys.")
    print("The most plausible decryptions will be displayed below:")
    print()
    for i in range(1, 26):
        result = ""
        for char in result:
            if char.isalpha():
                base = ord("a") if char.islower() else ord("A")
                result += chr((ord(char) - base - i) % 26 + base)
            else:
                result += char
        if check_plausibility(result):
            print(f"key of {i}: {result}")
            found = True
    if not found:
        print("No plausible decryptions found. Message may be too short to filter reliably.")
        if input("Would you like to see all possible decryptions? (y/n): ").lower() == 'y':
            for i in range(1, 26):
                result = ""
                for char in result:
                    if char.isalpha():
                        base = ord("a") if char.islower() else ord("A")
                        result += chr((ord(char) - base - i) % 26 + base)
                    else:
                        result += char
                print(f"key of {i}: {result}")
        else:
            print("Returning to main menu.")


def check_plausibility(result):
    letters = [char for char in result if char.isalpha()]
    # This function checks for common words or patterns in the decrypted message
    common_words = ["the", "and","you", "that", "was", "for", "are", "as", "with", "his", "they", "this", "from", "which", "but", "not", "all", "any", "she", "there", "when"]
    for word in common_words:
        if word in result.lower():
            return True
    # Check for a reasonable number of vowels in a row (not more than 3)
    vowel_run = 0
    for v in letters:
        if v in 'aeiou':
            vowel_run += 1
            if vowel_run > 3:
                return False
        else:
            vowel_run = 0
    # Check for a reasonable number of consonants in a row (not more than 5)
    consonant_run = 0
    for c in letters:
        if c not in 'aeiou':
            consonant_run += 1
            if consonant_run > 5:
                return False
        else:
            consonant_run = 0
    return True
"""