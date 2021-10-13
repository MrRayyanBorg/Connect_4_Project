#This class manages everything board related 
class Board:

  '''
  Functions Created:
    create_board()      - Creates the board aligning with custom column and row inputs.
    flip_board()        - Reverses the board along the Y-axis, makes chips start from bottom.
    print_board()       - Uses a for loop to output the boards current view.
    get_next_open_row() - Finds the untaken row, closest to the edge of the board.

  '''

  def create_board(rows,columns):
    board = [[0 for x in range(columns)] for y in range(rows)]
    return board

  def flip_board(board):
    board = board[::-1]
    return board

  def print_board(board):
    for i in board:
      print(i)

  def get_next_open_row(board, rows, columns):
    for row in range(rows):
      if board[row][columns] == 0:
        return row