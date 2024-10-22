import random
from math import gcd

# Step 1: Function to generate a large prime number (basic check)
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime_candidate(length):
    return random.getrandbits(length) | (1 << length - 1) | 1

def generate_prime_number(length=1024):
    candidate = generate_prime_candidate(length)
    while not is_prime(candidate):
        candidate = generate_prime_candidate(length)
    return candidate

# Step 2: Function to calculate modular inverse using Extended Euclidean Algorithm
def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Step 3: Key generation
def generate_keypair(keysize):
    p = generate_prime_number(keysize // 2)
    q = generate_prime_number(keysize // 2)
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)
    
    d = modinv(e, phi)
    
    return ((e, n), (d, n))

# Step 4: Encryption
def encrypt(public_key, plaintext):
    e, n = public_key
    plaintext_integers = [ord(char) for char in plaintext]
    ciphertext = [pow(m, e, n) for m in plaintext_integers]
    return ciphertext

# Step 5: Decryption
def decrypt(private_key, ciphertext):
    d, n = private_key
    decrypted_integers = [pow(c, d, n) for c in ciphertext]
    decrypted_message = ''.join([chr(m) for m in decrypted_integers])
    return decrypted_message

# Example usage
if __name__ == '__main__':
    keysize = 1024  # You can use 2048 for more security, but it will be slower.
    
    public_key, private_key = generate_keypair(keysize)
    
    message = "Hello, RSA!"
    print("Original message:", message)
    
    encrypted_message = encrypt(public_key, message)
    print("Encrypted message:", encrypted_message)
    
    decrypted_message = decrypt(private_key, encrypted_message)
    print("Decrypted message:", decrypted_message)
