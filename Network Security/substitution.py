import string

def generate_key():
    alphabet = string.ascii_lowercase
    shuffled_alphabet = list(alphabet)
    
    # Shuffle the alphabet for substitution
    import random
    random.shuffle(shuffled_alphabet)
    
    key = dict(zip(alphabet, shuffled_alphabet))
    return key

def encrypt(plaintext, key):
    encrypted_message = []
    for char in plaintext.lower():
        if char in key:
            encrypted_message.append(key[char])
        else:
            encrypted_message.append(char)
    return ''.join(encrypted_message)

def decrypt(ciphertext, key):
    reversed_key = {v: k for k, v in key.items()}
    decrypted_message = []
    for char in ciphertext:
        if char in reversed_key:
            decrypted_message.append(reversed_key[char])
        else:
            decrypted_message.append(char)
    return ''.join(decrypted_message)

key = generate_key()
print("Generated Key:", key)

plaintext = input("Enter plaintext: ")
ciphertext = encrypt(plaintext, key)
print("Encrypted:", ciphertext)

decrypted = decrypt(ciphertext, key)
print("Decrypted:", decrypted)
