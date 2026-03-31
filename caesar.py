print("Welcome to the Caesar Cipher Encryptor and Decryptor! This program allows you to encrypt and decrypt messages using the Caesar cipher. It also includes a feature to attempt to decrypt messages with an unknown key by trying all possible keys and checking for plausibility based on common words and letter patterns.")

# Function to perform Caesar cipher encryption or decryption based on the mode

from main import get_input
mode, message, key = get_input()

def mode_selection():
    if mode.lower() == 'e':
        encrypt_caesar(message, key, mode)
    elif mode.lower() == 'd':
        decrypt_caesar(message, key, mode)

def encrypt_caesar(message, key):
    encrypted_message = ""
    # Loop through each character in the input message
    for char in message:
        # Check if the character is an alphabetic character
        if char.isalpha():
            base = ord("a") if char.islower() else ord("A")                
            encrypted_message += chr((ord(char) - base + key) % 26 + base)
        else:
            encrypted_message += char


def decrypt_caesar(message, key):
    decrypted_message = ""
    if key == 0:
        force_decrypt(message)
    else:
        # Loop through each character in the input message
        for char in message:
            # Check if the character is an alphabetic character
            if char.isalpha():
                base = ord("a") if char.islower() else ord("A")
                decrypted_message += chr((ord(char) - base - key) % 26 + base)
            # If the character is not alphabetic, add it to the decrypted_message without changing it
            else:
                decrypted_message += char

 
def force_decrypt(encrypted_message):
    found = False
    print("Attempting to force decrypt the message with all possible keys.")
    print("The most plausible decryptions will be displayed below:")
    print()
    for i in range(1, 26):
        decrypted_message = ""
        for char in encrypted_message:
            if char.isalpha():
                base = ord("a") if char.islower() else ord("A")
                decrypted_message += chr((ord(char) - base - i) % 26 + base)
            else:
                decrypted_message += char
        if check_plausibility(decrypted_message):
            print(f"key of {i}: {decrypted_message}")
            found = True
    if not found:
        print("No plausible decryptions found. Message may be too short to filter reliably.")
        if input("Would you like to see all possible decryptions? (y/n): ").lower() == 'y':
            for i in range(1, 26):
                decrypted_message = ""
                for char in encrypted_message:
                    if char.isalpha():
                        base = ord("a") if char.islower() else ord("A")
                        decrypted_message += chr((ord(char) - base - i) % 26 + base)
                    else:
                        decrypted_message += char
                print(f"key of {i}: {decrypted_message}")
        else:
            print("Returning to main menu.")



def check_plausibility(decrypted_message):
    letters = [char for char in decrypted_message if char.isalpha()]
    # This function checks for common words or patterns in the decrypted message
    common_words = ["the", "and","you", "that", "was", "for", "are", "as", "with", "his", "they", "this", "from", "which", "but", "not", "all", "any", "she", "there", "when"]
    for word in common_words:
        if word in decrypted_message.lower():
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