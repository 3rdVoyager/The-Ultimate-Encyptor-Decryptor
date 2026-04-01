print("Welcome to the Ultimate Encryptonator and Decryptonator! This program allows you to encrypt and decrypt messages using many different ciphers. You can choose which cipher to use and follow the prompts to encrypt or decrypt messages. Let's get started!")

# Declare variables to store user input
def declare_variables():
    global start, cipher, mode, message, key, encrypted_message, decrypted_message
    cipher = ""
    mode = ""
    message = ""
    key = ""
    encrypted_message = ""
    decrypted_message = ""

# This function gets user input for the cipher, mode, message, and key, and imports the appropriate cipher module based on the user's choice. It also includes error handling to ensure that the user inputs valid choices for each prompt.
def get_input(start, cipher, mode, message, key):
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
        # Prompt the user to enter a key, and if the cipher is Caesar, ensure that the key is a valid integer. If the cipher is Vigenère, ensure that the key is a non-empty string.
        key = get_key()
        return cipher, mode, message, key

# This function prompts the user to enter a key for the chosen cipher, and includes error handling to ensure that the key is valid based on the requirements of the chosen cipher.
def get_key():
    if cipher == 'c':
        while True:
            key = input("Enter the key (a number between 1 and 25): ")
            if key.isdigit() and 1 <= int(key) <= 25:
                return key
            else:
                print("Invalid key. Please enter a number between 1 and 25.")
    elif cipher == 'v':
        while True:
            key = input("Enter the keyword (a non-empty string): ").strip()
            if key.isalpha():
                return key
            else:                
                print("Invalid key. Please enter a non-empty string consisting of letters only.")

# This function takes the user's choices for cipher, mode, message, and key, and calls the appropriate encryption or decryption function from the corresponding cipher module. It then displays the result to the user.
def encrypt_decrypt(cipher, mode, message, key, encrypted_message, decrypted_message):
    if cipher == 'c':
        import caesar
        if mode == 'e':
            encrypted_message = caesar.encrypt_caesar(message, int(key))
        elif mode == 'd':
            decrypted_message = caesar.decrypt_caesar(message, int(key))
    elif cipher == 'v':
        import vigenere
        if mode == 'e':
            encrypted_message = vigenere.encrypt_vigenere(message, key)
        elif mode == 'd':
            decrypted_message = vigenere.decrypt_vigenere(message, key)
    display_result(encrypted_message, decrypted_message)

# This function displays the result of the encryption or decryption process to the user, based on the chosen cipher and mode. It takes the cipher, mode, encrypted message, and decrypted message as parameters and prints the appropriate result to the console.
def display_result(encrypted_message, decrypted_message):
    if mode == 'e':
        print(f"Encrypted message: {encrypted_message}")
    elif mode == 'd':
        print(f"Decrypted message: {decrypted_message}")

declare_variables()
cipher, mode, message, key = get_input("", cipher, mode, message, key)
# Import the appropriate cipher module based on the user's choice
encrypt_decrypt(cipher, mode, message, key, encrypted_message, decrypted_message)