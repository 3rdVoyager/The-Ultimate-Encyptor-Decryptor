print("Welcome to the Ultimate Encryptonator and Decryptonator! This program allows you to encrypt and decrypt messages using many different ciphers. You can choose which cipher to use and follow the prompts to encrypt or decrypt messages. Let's get started!")

# This function gets user input for the cipher, mode, message, and key, and imports the appropriate cipher module based on the user's choice. It also includes error handling to ensure that the user inputs valid choices for each prompt.
def get_input():
    # Declare variables to store user input
    start = ""
    cipher = ""
    mode = ""
    message = ""
    key = ""
    # Prompt the user to start a new session or quit, and repeat until a valid choice is made
    while start.strip().lower() not in ['c', 'q']:
        start = input("Type 'c' to start a new encryption/decryption session or type 'q' to quit: ").strip().lower()
        if start in ['c', 'q']:
            break
        else:
            print("Invalid input. Please try again.")
    # If the user chooses to quit, print a goodbye message and exit the program. If they choose to start a new session, prompt them to choose a cipher and mode, and then import the appropriate cipher module.
    if start.lower() == 'q':
        print("Goodbye!")
        print("Created by Joshua Cheng in March 2026.")
        print("Program exited.")
        exit()
    # If the user chooses to start a new session, prompt them to choose a cipher and mode, and then import the appropriate cipher module.
    elif start.lower() == 'c':
        # Prompt the user to choose a cipher and repeat until a valid choice is made
        while cipher.strip().lower() not in ['c', 'v']:
            cipher = input("Choose a cipher: Caesar (c), Vigenère (v):").strip().lower()
            if cipher in ['c', 'v']:
                break
            else:
                print("Invalid choice. Please try again.")
        #prompt the user to choose a mode and repeat until a valid choice is made
        while mode.strip().lower() not in ['e', 'd']:
            mode=input("Do you want to encrypt or decrypt a message? (e/d): ").strip().lower()
            if mode in ['e', 'd']:
                break
            else:
                print("Invalid choice. Please try again.")
        # Prompt the user to enter a message and key
        message = input("Enter the message: ")
        key = input("Enter the key: ")
        # Import the appropriate cipher module based on the user's choice
        import_cipher(cipher)
        return mode, message, key

def import_cipher(cipher):
    if cipher == 'c':
        import caesar
        return caesar
    elif cipher == 'v':
        import vigenere
        return vigenere

get_input()