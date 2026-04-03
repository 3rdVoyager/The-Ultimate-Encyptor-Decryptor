# Function to perform Caesar cipher encryption or decryption based on the mode

def encrypt_caesar(message, key):
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


def decrypt_caesar(message, key):
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