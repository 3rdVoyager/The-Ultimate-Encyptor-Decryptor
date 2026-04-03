import string

alphabet = string.ascii_lowercase

def encrypt_substitution(message, key):
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


def decrypt_substitution(message, key):
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