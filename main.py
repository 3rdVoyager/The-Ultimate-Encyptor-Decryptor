print("Welcome to the Ultimate Encryptonator and Decryptonator! This program allows you to encrypt and decrypt messages using many different ciphers. You can choose which cipher to use and follow the prompts to encrypt or decrypt messages. Let's get started!")

import sys
import caesar

# This function gets user input for the cipher, mode, message, and key, and imports the appropriate cipher module based on the user's choice. It also includes error handling to ensure that the user inputs valid choices for each prompt.
def get_input():
    # Prompt the user to start a new session or quit, and repeat until a valid choice is made
    while True:
        start = input("Type 'c' to start a new encryption/decryption session or type 'q' to quit: ").strip().lower()
        if start in ['c', 'q']:
            break
        else:
            print("Invalid input. Please try again.")
    # If the user chooses to quit, print a goodbye message and exit the program. If they choose to start a new session, prompt them to choose a cipher and mode, and then import the appropriate cipher module.
    if start == 'q':
        exit_program()
    # If the user chooses to start a new session, prompt them to choose a cipher and mode, and then import the appropriate cipher module.
    elif start == 'c':
        # Prompt the user to choose a cipher and repeat until a valid choice is made
        while True:
            cipher = input("Choose a cipher: Caesar (c), Vigenère (v):").strip().lower()
            if cipher in ['c', 'v']:
                break
            print("Invalid choice. Please try again.")
        #prompt the user to choose a mode and repeat until a valid choice is made
        while True:
            mode=input("Do you want to encrypt or decrypt a message? (e/d): ").strip().lower()
            if mode in ['e', 'd']:
                break
            print("Invalid choice. Please try again.")
        # Prompt the user to enter a message and key
        message = input("Enter the message: ")
        # Prompt the user to enter a key, and if the cipher is Caesar, ensure that the key is a valid integer. If the cipher is Vigenère, ensure that the key is a non-empty string.
        key = get_key(cipher)
        return cipher, mode, message, key

# This function prompts the user to enter a key for the chosen cipher, and includes error handling to ensure that the key is valid based on the requirements of the chosen cipher.
def get_key(cipher):
    if cipher.lower() == 'c':
        while True:
            key = input("Enter the key (a number between 1 and 25): ")
            if key.isdigit() and 1 <= int(key) <= 25:
                return key
            else:
                print("Invalid key. Please enter a number between 1 and 25.")
    elif cipher.lower() == 'v':
        while True:
            key = input("Enter the keyword (a non-empty string): ").strip()
            if key.isalpha():
                return key
            else:                
                print("Invalid key. Please enter a non-empty string consisting of letters only.")

# This function takes the user's choices for cipher, mode, message, and key, and calls the appropriate encryption or decryption function from the corresponding cipher module. It then displays the result to the user.
def encrypt_decrypt(cipher, mode, message, key):
    result = ""
    if cipher == 'c':
        if mode == 'e':
            result = caesar.encrypt_caesar(message, int(key))
        elif mode == 'd':
            result = caesar.decrypt_caesar(message, int(key))
    elif cipher == 'v':
        if mode == 'e':
            result = vigenere.encrypt_vigenere(message, key)
        elif mode == 'd':
            result = vigenere.decrypt_vigenere(message, key)
    display_result(mode, result)

# This function displays the result of the encryption or decryption process to the user, based on the chosen cipher and mode. It takes the cipher, mode, encrypted message, and decrypted message as parameters and prints the appropriate result to the console.
def display_result(mode, result):
    if mode == 'e':
        print(f"Encrypted message: {result}")
    elif mode == 'd':
        print(f"Decrypted message: {result}")

def exit_program():
    print("Goodbye!")
    print("Created by Joshua Cheng.")
    print("Program exited.")
    sys.exit()

while True:
    cipher, mode, message, key = get_input()
    encrypt_decrypt(cipher, mode, message, key)