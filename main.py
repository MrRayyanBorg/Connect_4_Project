#Module Import
from Modules.board import Board

ROW_COUNT = 6
COLUMN_COUNT = 7

def add_chip(board, row, input_column, chip): 
  #Updates the board with locations of chips for each player
  board[row][input_column] = chip

def is_valid_location(board, input_column):
  #this function validates if the first row is free in the input column
  return board[ROW_COUNT-1][input_column] == 0

board = Board.create_board(ROW_COUNT,COLUMN_COUNT) #creates the game board
Board.print_board(board) #outputs the board

game_over = False #game over variable
turn = 0 #alternating turn between players

while not game_over: #This will continue running until the game is over

  #Player1 turn
  if turn == 0:
    #taking input from the user as int
    input_column = int(input("Player 1 - Make your selection (0-6):")) 

    if is_valid_location(board, input_column):
      row = Board.get_next_open_row(board, ROW_COUNT, input_column)
      add_chip(board, row, input_column, 1)

  #Player2 turn
  else:
    input_column = int(input("Player 2 - Make your selection (0-6):")) 

    if is_valid_location(board, input_column):
      row = Board.get_next_open_row(board, ROW_COUNT, input_column)
      add_chip(board, row, input_column, 2)
  
  Board.print_board(board)
  #alternates the turns between player 1 and player 2
  turn += 1
  turn %= 2