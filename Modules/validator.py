#This class manages everything realted to rules and validation 
class Validator:

  '''
  Functions Created:
    validate_column() - This function validates if the first row is free in the input column.

  '''
  def validate_column(board, rows, columns):
    return board[rows-1][columns] == 0
  
  def validate_win(board, rows, columns, chip):
    # Search horizontal connect four
    for c in range(columns-3): 
      for r in range(rows):
        if board[r][c] == chip and board[r][c+1] == chip and board[r][c+2] == chip and board[r][c+3] == chip:
          return True

    # Search vertical connect four
    for c in range(columns): 
      for r in range(rows-3):
        if board[r][c] == chip and board[r+1][c] == chip and board[r+2][c] == chip and board[r+3][c] == chip:
          return True
    
    # Search Upward Diagonal connect four 
    for c in range(columns-3): 
      for r in range(rows-3):
        if board[r][c] == chip and board[r+1][c+1] == chip and board[r+2][c+2] == chip and board[r+3][c+3] == chip:
          return True
    
    # Search Downward Diagonal connect four 
    for c in range(columns-3): 
      for r in range(3,rows):
        if board[r][c] == chip and board[r-1][c+1] == chip and board[r-2][c+2] == chip and board[r-3][c+3] == chip:
          return True
