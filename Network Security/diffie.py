import random

# Function to perform modular exponentiation
def mod_exp(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:  # If exp is odd, multiply base with result
            result = (result * base) % mod
        exp = exp // 2  # Divide the exponent by 2
        base = (base * base) % mod  # Square the base
    return result

# Diffie-Hellman Key Exchange
def diffie_hellman(p, g):
    # Private keys for Alice and Bob (chosen randomly)
    a = random.randint(2, p - 2)
    b = random.randint(2, p - 2)

    # Public keys for Alice and Bob
    A = mod_exp(g, a, p)  # Alice's public key
    B = mod_exp(g, b, p)  # Bob's public key

    # Shared secret computation
    shared_secret_Alice = mod_exp(B, a, p)  # Alice computes the shared secret
    shared_secret_Bob = mod_exp(A, b, p)  # Bob computes the shared secret

    return A, B, shared_secret_Alice, shared_secret_Bob


p = 23  # Small prime for simplicity
g = 5   # Primitive root modulo p

# Perform Diffie-Hellman key exchange
A, B, shared_secret_Alice, shared_secret_Bob = diffie_hellman(p, g)

print("Public key of Alice (A):", A)
print("Public key of Bob (B):", B)
print("Shared secret (calculated by Alice):", shared_secret_Alice)
print("Shared secret (calculated by Bob):", shared_secret_Bob)