import numpy as np

class Board:

  #this function creates a board along an x,y
  def create_board(rows,columns):
    board = np.zeros((rows,columns)) #creates board 6 by 7
    return board

  #this function outputs the board on a flipped axis
  def print_board(board):
    print(np.flip(board, 0))

  def get_next_open_row(board, rows, input_column):
  #this function checks which row is not taken, closest to the first row and within input column
    for row in range(rows):
      if board[row][input_column] == 0:
        return row