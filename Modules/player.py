#This class manages everything board related 
class Player:

  '''
  Functions Created:
    add_chip()          - Updates the board with locations of chips for each player.

  '''
  def is_valid_location(board, rows, column):
  #this function validates if the first row is free in the input column
    return board[rows-1][column] == 0

  def add_chip(board, row, column, chip):
    board[row][column] = chip