def generate_key(message, key):
    key = list(key)
    if len(message) == len(key):
        return key
    else:
        for i in range(len(message) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def encrypt_vigenere(message, key):
    encrypted_message = []
    key = generate_key(message, key)
    for i in range(len(message)):
        char = message[i]
        if char.isupper():
            encrypted_char = chr((ord(char) + ord(key[i]) - 2 * ord('A')) % 26 + ord('A'))
        elif char.islower():
            encrypted_char = chr((ord(char) + ord(key[i]) - 2 * ord('a')) % 26 + ord('a'))
        else:
            encrypted_char = char
        encrypted_message.append(encrypted_char)
    return "".join(encrypted_message)

def decrypt_vigenere(message, key):
    decrypted_message = []
    key = generate_key(message, key)
    for i in range(len(message)):
        char = message[i]
        if char.isupper():
            decrypted_char = chr((ord(char) - ord(key[i]) + 26) % 26 + ord('A'))
        elif char.islower():
            decrypted_char = chr((ord(char) - ord(key[i]) + 26) % 26 + ord('a'))
        else:
            decrypted_char = char
        decrypted_message.append(decrypted_char)
    return "".join(decrypted_message)

# Example usage

print("Welcome to the Vigenère Cipher Encryptor and Decryptor! This program allows you to encrypt and decrypt messages using a keyword. Let's get started!")

def get_input():
    start=input("Type 'c' to start a new session or 'q' to quit: ")
    if start.lower() == 'q':
        print("Goodbye!")
        print("Created by Joshua Cheng.")
        print("Program exited.")
        exit()
    elif start.lower() == 'c':
        mode = input("Do you want to encrypt or decrypt a message? (e/d): ").strip().lower()
        if mode in ['e', 'd']:
            message = input("Enter the message to encrypt: ")
            key = input("Enter the keyword: ")
            return mode, message, key
        else:
            print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")
    else:
        print("Invalid input. Please try again.")
        return get_input()

mode, message, key = get_input()

while True:
    if mode == 'e':
        encrypted_message = encrypt_vigenere(message, key)
        print(f"Encrypted message: {encrypted_message}")
        mode, message, key = get_input()
    elif mode == 'd':
        decrypted_message = decrypt_vigenere(message, key)
        print(f"Decrypted message: {decrypted_message}")
        mode, message, key = get_input()
    else:
        print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")
        mode, message, key = get_input()