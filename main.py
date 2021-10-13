#Module Import
from Modules.board import Board

ROW_COUNT = 6
COLUMN_COUNT = 7

def add_chip(board, row, selected_column, chip): 
  #Updates the board with locations of chips for each player
  print(board[row][selected_column])
  print("coc")

def is_valid_location(board, selected_column):
  #this function validates if the first row is free in the input column
  return board[ROW_COUNT-1][selected_column] == 0

board = Board()
board_axis = board.create_board(ROW_COUNT,COLUMN_COUNT) #creates the game board
board.print_board() #outputs the board

game_over = False #game over variable
turn = 0 #alternating turn between players

while not game_over: #This will continue running until the game is over

  #Player1 turn
  if turn == 0:
    #taking input from the user as int
    selected_column = int(input("Player 1 - Make your selection (0-6):")) 

    if is_valid_location(board_axis, selected_column):
      row = board.get_next_open_row(ROW_COUNT, selected_column)
      add_chip(board_axis, row, selected_column, 1)

  #Player2 turn
  else:
    selected_column = int(input("Player 2 - Make your selection (0-6):")) 

    if is_valid_location(board_axis, selected_column):
      row = board.get_next_open_row(board_axis, ROW_COUNT, selected_column)
      add_chip(board_axis, row, selected_column, 2)
  
  board.print_board()
  #alternates the turns between player 1 and player 2
  turn += 1
  turn %= 2