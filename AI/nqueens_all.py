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

def helper(board, col, solutions) -> None:
    if col >= len(board):
      solutions.append([row[:] for row in board])
      return # base case
    for row in range(len(board)):
        square = [row, col]
        if valid(board, square):
            board[row][col] = 'Q'
            helper(board, col + 1, solutions)
            board[row][col] = '_'

n = int(input("Enter no. of queens: "))
board = [['_' for i in range(n)] for j in range(n)]
solutions = []
helper(board, 0, solutions)
for solution in solutions:
  print('\nSolution: ')
  display(solution)