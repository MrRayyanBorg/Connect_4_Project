class Board:

  #this function creates a board along an x,y
  def create_board(rows,columns):
    #board = np.zeros((rows,columns)) #creates board 6 by 7
    board = [[0 for x in range(columns)] for y in range(rows)]
    return board

  #this function outputs the board on a flipped axis
  def print_board(board):
    board = board[::-1]
    for i in board:
      print(i)

  def get_next_open_row(board, rows, input_column):
  #this function checks which row is not taken, closest to the first row and within input column
    for row in range(rows):
      if board[row][input_column] == 0:
        return row