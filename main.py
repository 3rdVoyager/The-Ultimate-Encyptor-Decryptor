import caesar

print("Welcome to the Ultimate Encryptonator and Decryptonator! This program allows you to encrypt and decrypt messages using many different ciphers. You can choose which cipher to use and follow the prompts to encrypt or decrypt messages. Let's get started!")

def get_input():
    start=input("Type 'c' to start a new session, 'i' to see instructions, or 'q' to quit: ")
    # Handle user input for starting, instructions, or quitting the program
    if start.lower() == 'q':
        print("Goodbye!")
        print("Created by Joshua Cheng.")
        print("Program exited.")
        exit()
    elif start.lower() == 'i':
        print("Instructions: To start a new session, type 'c'. You will then be prompted to choose a cipher, whether to encrypt or decrypt, and to enter the necessary information for the chosen cipher. Follow the prompts to see your encrypted or decrypted message. After each operation, you will have the option to continue or exit the program.")
        return get_input()
    elif start.lower() == 'c':
        cipher = input("Choose a cipher - Caesar (c), Vigenère (v):").lower()
        if cipher == 'c':
            return get_caesar_input()
        elif cipher == 'v':
            return get_vigenere_input()
        else:
            print("Invalid choice. Please choose 'c' for Caesar or 'v' for Vigenère.")
            return get_input()
    else:
        print("Invalid input. Please try again.")
        return get_input()