def encrypt_rail_fence_cipher(text, key):
    # Create an empty 2D array for the rail matrix
    rail = [['\n' for i in range(len(text))] for j in range(key)]
    
    # Set the direction (downward or upward)
    dir_down = False
    row, col = 0, 0
    
    for i in range(len(text)):
        if row == 0 or row == key - 1:
            dir_down = not dir_down
        
        # Place the character in the correct rail
        rail[row][col] = text[i]
        col += 1
        
        # Move to the next row in the correct direction
        if dir_down:
            row += 1
        else:
            row -= 1
    
    # Read the matrix to get the encrypted message
    encrypted_text = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                encrypted_text.append(rail[i][j])
    
    return "".join(encrypted_text)

def decrypt_rail_fence_cipher(cipher, key):
    # Create an empty 2D array for the rail matrix
    rail = [['\n' for i in range(len(cipher))] for j in range(key)]
    
    # Mark the positions in the matrix to be filled
    dir_down = None
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        
        rail[row][col] = '*'
        col += 1
        
        if dir_down:
            row += 1
        else:
            row -= 1
    
    # Fill the marked positions with cipher characters
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1
    
    # Read the matrix to construct the decrypted message
    decrypted_text = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        
        if rail[row][col] != '*':
            decrypted_text.append(rail[row][col])
            col += 1
        
        if dir_down:
            row += 1
        else:
            row -= 1
    
    return "".join(decrypted_text)

# Example usage:
message = "meowmeow"
key = 3

encrypted = encrypt_rail_fence_cipher(message.replace(" ", ""), key)
print("Encrypted:", encrypted)

decrypted = decrypt_rail_fence_cipher(encrypted, key)
print("Decrypted:", decrypted)
