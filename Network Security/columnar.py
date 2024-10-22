def encrypt_columnar_transposition_cipher(message, key):
    # Remove spaces from the message
    message = message.replace(" ", "")
    
    # Calculate the number of rows and columns needed for the message
    num_rows = len(message) // len(key) + (len(message) % len(key) > 0)
    num_cols = len(key)
    
    # Create a matrix to hold the encrypted message
    matrix = [['' for _ in range(num_cols)] for _ in range(num_rows)]
    
    # Fill the matrix row by row
    index = 0
    for row in range(num_rows):
        for col in range(num_cols):
            if index < len(message):
                matrix[row][col] = message[index]
                index += 1
    
    # Sort the columns based on the key
    sorted_key_indices = sorted(range(len(key)), key=lambda k: key[k])
    
    # Create the encrypted message by reading the columns in the order of the key
    encrypted_message = ''
    for col in sorted_key_indices:
        for row in range(num_rows):
            if matrix[row][col]:
                encrypted_message += matrix[row][col]
    
    return encrypted_message

def decrypt_columnar_transposition_cipher(encrypted_message, key):
    # Calculate the number of rows and columns needed
    num_cols = len(key)
    num_rows = len(encrypted_message) // num_cols
    
    # Sort the columns based on the key
    sorted_key_indices = sorted(range(len(key)), key=lambda k: key[k])
    
    # Create a matrix to hold the decrypted message
    matrix = [['' for _ in range(num_cols)] for _ in range(num_rows)]
    
    # Fill the matrix column by column based on the sorted key
    index = 0
    for col in sorted_key_indices:
        for row in range(num_rows):
            if index < len(encrypted_message):
                matrix[row][col] = encrypted_message[index]
                index += 1
    
    # Read the message row by row
    decrypted_message = ''
    for row in range(num_rows):
        for col in range(num_cols):
            if matrix[row][col]:
                decrypted_message += matrix[row][col]
    
    return decrypted_message

message = "we are discovered"
key = "3142"

encrypted = encrypt_columnar_transposition_cipher(message, key)
print(f"Encrypted: {encrypted}")

decrypted = decrypt_columnar_transposition_cipher(encrypted, key)
print(f"Decrypted: {decrypted}")
