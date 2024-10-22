import random

def generate_key(length):
    # Generates a random key of the same length as the plaintext
    key = ''.join(random.choice('01') for _ in range(length))
    return key

def text_to_binary(text):
    # Converts each character in the text to its 8-bit binary equivalent
    binary = ''.join(format(ord(c), '08b') for c in text)
    return binary

def binary_to_text(binary):
    # Converts binary back to text by grouping into 8-bit chunks
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    text = ''.join(chr(int(c, 2)) for c in chars)
    return text

def vernam_encrypt(plaintext, key):
    # Convert plaintext and key to binary
    plaintext_bin = text_to_binary(plaintext)
    key_bin = key[:len(plaintext_bin)]  # Ensure the key matches the length of the binary plaintext

    # Perform XOR on each bit
    ciphertext_bin = ''.join(str(int(p) ^ int(k)) for p, k in zip(plaintext_bin, key_bin))

    return ciphertext_bin

def vernam_decrypt(ciphertext_bin, key):
    # Perform XOR on each bit to get the original binary plaintext
    decrypted_bin = ''.join(str(int(c) ^ int(k)) for c, k in zip(ciphertext_bin, key))
    
    # Convert binary back to plaintext
    plaintext = binary_to_text(decrypted_bin)
    
    return plaintext

# Example usage
message = "HELLO"
binary_key = generate_key(len(text_to_binary(message)))

print("Original message:", message)
print("Generated binary key:", binary_key)

ciphertext = vernam_encrypt(message, binary_key)
print("Ciphertext (binary):", ciphertext)

decrypted_message = vernam_decrypt(ciphertext, binary_key)
print("Decrypted message:", decrypted_message)
