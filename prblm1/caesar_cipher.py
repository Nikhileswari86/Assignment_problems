def caesar_cipher_encrypt(message, shift):
    encrypted = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted


def caesar_cipher_decrypt(message, shift):
    return caesar_cipher_encrypt(message, -shift)



if __name__ == "__main__":
    
    message = input("Enter the message: ")
    shift = int(input("Enter the shift (e.g. 3): "))

    
    encrypted_message = caesar_cipher_encrypt(message, shift)
    print("Encrypted Message:", encrypted_message)

    
    decrypted_message = caesar_cipher_decrypt(encrypted_message, shift)
    print("Decrypted Message:", decrypted_message)
