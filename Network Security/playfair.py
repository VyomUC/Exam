# Function to generate the Playfair cipher key matrix
def generate_key_matrix(key):
    # Remove duplicates from the key
    key = "".join(dict.fromkeys(key.replace("J", "I")))
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    
    # Add remaining letters from the alphabet to the key
    matrix_key = key + "".join([ch for ch in alphabet if ch not in key])
    
    # Create a 5x5 matrix
    matrix = [list(matrix_key[i:i+5]) for i in range(0, 25, 5)]
    return matrix

# Function to prepare the text by pairing the letters
def prepare_text(text):
    text = text.upper().replace("J", "I").replace(" ", "")
    prepared = ""
    
    i = 0
    while i < len(text):
        prepared += text[i]
        if i + 1 < len(text) and text[i] == text[i + 1]:
            prepared += "X"  # Insert 'X' between repeated letters
            i += 1
        elif i + 1 < len(text):
            prepared += text[i + 1]
            i += 2
        else:
            prepared += "X"  # Add 'X' if there's an odd number of characters
            i += 1
    
    return prepared

# Function to find the position of a letter in the matrix
def find_position(matrix, letter):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return row, col
    return None

# Function to encrypt a pair of letters
def encrypt_pair(matrix, pair):
    row1, col1 = find_position(matrix, pair[0])
    row2, col2 = find_position(matrix, pair[1])
    
    if row1 == row2:
        # Same row, move right
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:
        # Same column, move down
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    else:
        # Rectangle, swap columns
        return matrix[row1][col2] + matrix[row2][col1]

# Function to encrypt the text using Playfair cipher
def playfair_encrypt(text, key):
    matrix = generate_key_matrix(key)
    prepared_text = prepare_text(text)
    
    encrypted_text = ""
    for i in range(0, len(prepared_text), 2):
        encrypted_text += encrypt_pair(matrix, prepared_text[i:i+2])
    
    return encrypted_text

# Example usage
key = "PLAYFAIRCIPHER"
text = "HELLO WORLD"
encrypted = playfair_encrypt(text, key)
print("Encrypted Text:", encrypted)
