print("Welcome to the Ultimate Encryptonator and Decryptonator! This program allows you to encrypt and decrypt messages using many different ciphers. You can choose which cipher to use and follow the prompts to encrypt or decrypt messages. Let's get started!")

def get_input():
    start=input("Type 'c' to start a new encryption/decryption session or type 'q' to quit: ")
    if start.lower() == 'q':
        print("Goodbye!")
        print("Created by Joshua Cheng in March 2026.")
        print("Program exited.")
        exit()
    elif start.lower() == 'c':
        cipher = input("Choose a cipher: Caesar (c), Vigenère (v):").lower()
        if cipher == 'c':
            import caesar
        elif cipher == 'v':
            import vigenere
        else:
            print("Invalid choice. Please try again.")
            return get_input()
        mode=input("Do you want to encrypt or decrypt a message? (e/d): ").strip().lower()
        if mode in ['e', 'd']:
            message = input("Enter the message: ")
            key = input("Enter the key: ")
            return mode, message, key
    else:
        print("Invalid input. Please try again.")
        return get_input()

get_input()