def display(board) -> None:
    for row in board:
        for col in row:
            print(col, end = '\t')
        print('\n')

def valid(board, square) -> bool:
    # Row
    [row, col] = square
    for i in range(col):
        if board[row][i] == 'Q': return False

    # Bottom left diagonal
    while row < len(board) and col >= 0:
        if board[row][col] == 'Q': return False
        row += 1
        col -= 1

    # Upper left diagonal
    [row, col] = square
    while row >= 0 and col >= 0:
        if board[row][col] == 'Q': return False
        row -= 1
        col -= 1

    return True

def helper(board, col) -> bool:
    if col >= len(board): return True # base case
    for row in range(len(board)):
        square = [row, col]
        if valid(board, square):
            board[row][col] = 'Q'
            if helper(board, col + 1): return True
            board[row][col] = '_' # backtrack
    return False

n = int(input("Enter no. of queens: "))
board = [['_' for i in range(n)] for j in range(n)]
if helper(board, 0):
    print(f'\nChess Board with {n} Queens: ')
    display(board)
else: print('\nNo solution')