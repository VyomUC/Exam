def displayMatrix(grid):
  for i in range(26):
    for j in range(26):
      print(grid[i][j], end = ' ')
    print()

def getMatrix():
  letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  grid = [['_' for _ in range(26)] for _ in range(26)]
  start = 0
  for row in range(26):
    ptr = start
    for col in range(26):
      grid[row][col] = letters[ptr]
      ptr = (ptr + 1) % 26
    start += 1
  return grid

def padKey(text, key):
  newkey = ''
  ptr = 0
  for _ in text:
    newkey += key[ptr]
    ptr = (ptr + 1) % len(key)
  return newkey


def encrypt(plaintext, key, grid):
  key = padKey(plaintext, key)
  ciphertext = ''

  for i in range(len(plaintext)):
    if plaintext[i].isalpha():
      row = ord(key[i]) - ord('A')
      col = ord(plaintext[i]) - ord('A')
      ciphertext += grid[row][col]
    else: ciphertext += plaintext[i]
  return ciphertext

def decrypt(ciphertext, key, grid):
  key = padKey(ciphertext, key)
  plaintext = ''

  for i in range(len(ciphertext)):
    row = ord(key[i]) - ord('A')
    if ciphertext[i].isalpha():
      for j in range(26):
        if grid[row][j] == ciphertext[i]:
          plaintext += chr(j + ord('A'))
          break
    else: plaintext += ciphertext[i]
  return plaintext

text = input("Enter message: ").upper()
key = input("Enter keyword: ").upper()

if len(key) > len(text):
  print("Invalid key")
  exit()

grid = getMatrix()
e = encrypt(text, key, grid)
print(f"\nEncrypted message: {e}")
d = decrypt(e, key, grid)
print(f"Decrypted message: {d}")

# plaintext = HELLOWORLD
# key = KEY
# ciphertext = RIJVSUYVJN