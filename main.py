#Module Import
from Modules.board import Board
from Modules.player import Player
from Modules.validator import Validator

ROW_COUNT = 6
COLUMN_COUNT = 7
PLAYER1_ID = 1
PLAYER2_ID = 2

board = Board.create_board(ROW_COUNT,COLUMN_COUNT)
Board.print_board(Board.flip_board(board))

game_over = False #game over variable
turn = 0 #alternating turn between players

while not game_over: #This will continue running until the game is over

  #Player1 turn
  if turn == 0:
    #taking input from the user as int
    input_column = int(input("Player 1 - Make your selection (0-6):")) 

    while not Validator.validate_column(board, ROW_COUNT, input_column):
      print('This column is full. Please select another.')
      input_column = int(input("Player 2 - Make your selection (0-6):"))

    else:
      chip_slot = Board.get_next_open_row(board, ROW_COUNT, input_column)
      Player.add_chip(board, chip_slot, input_column, PLAYER1_ID)

      if Validator.validate_win(board,ROW_COUNT,COLUMN_COUNT,PLAYER1_ID) == True:
        Player.player_win(PLAYER1_ID)
        game_over = True
        break

  #Player2 turn
  else:
    input_column = int(input("Player 2 - Make your selection (0-6):")) 

    while not Validator.validate_column(board, ROW_COUNT, input_column):
      print('This column is full. Please select another.')
      input_column = int(input("Player 2 - Make your selection (0-6):"))
      
    else:
      chip_slot = Board.get_next_open_row(board, ROW_COUNT, input_column)
      Player.add_chip(board, chip_slot, input_column, PLAYER2_ID)

      if Validator.validate_win(board,ROW_COUNT,COLUMN_COUNT,PLAYER2_ID) == True:
        Player.player_win(PLAYER2_ID)
        game_over = True
        break
  
  Board.print_board(Board.flip_board(board))

  #alternates the turns between player 1 and player 2
  turn += 1
  turn %= 2