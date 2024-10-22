# pip install cryptography

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

# AES encryption
def encrypt_aes(key, plaintext):
    # Generate a random 16-byte IV (Initialization Vector)
    iv = os.urandom(16)
    
    # Create a Cipher object
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    
    # Pad the plaintext to make it a multiple of the block size (16 bytes for AES)
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_plaintext = padder.update(plaintext) + padder.finalize()
    
    # Encrypt the padded plaintext
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()
    
    return iv + ciphertext  # Return IV + ciphertext for proper decryption

# AES decryption
def decrypt_aes(key, ciphertext):
    # Split the IV and ciphertext
    iv = ciphertext[:16]
    actual_ciphertext = ciphertext[16:]
    
    # Create a Cipher object
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    
    # Decrypt the ciphertext
    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(actual_ciphertext) + decryptor.finalize()
    
    # Unpad the plaintext
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
    
    return plaintext

key = os.urandom(32)  # AES-256 requires a 32-byte key
plaintext = b"This is a secret message"

# Encrypt the message
ciphertext = encrypt_aes(key, plaintext)
print("Ciphertext:", ciphertext)

# Decrypt the message
decrypted_text = decrypt_aes(key, ciphertext)
print("Decrypted:", decrypted_text)
