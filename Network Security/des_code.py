# pip install pycryptodome

# Required Libraries
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

# Key and Block Size (DES uses 8-byte blocks and keys)
BLOCK_SIZE = 8

# Function to encrypt data
def des_encrypt(plain_text, key):
    des = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plain_text.encode('utf-8'), BLOCK_SIZE)
    encrypted_text = des.encrypt(padded_text)
    return encrypted_text

# Function to decrypt data
def des_decrypt(encrypted_text, key):
    des = DES.new(key, DES.MODE_ECB)
    decrypted_text = unpad(des.decrypt(encrypted_text), BLOCK_SIZE)
    return decrypted_text.decode('utf-8')

# Example usage:
if __name__ == "__main__":
    key = b'8bytekey'  # DES requires an 8-byte key
    plain_text = "Hello, DES!"
    
    # Encrypting the plain text
    encrypted_text = des_encrypt(plain_text, key)
    print(f"Encrypted: {encrypted_text}")
    
    # Decrypting back to plain text
    decrypted_text = des_decrypt(encrypted_text, key)
    print(f"Decrypted: {decrypted_text}")
