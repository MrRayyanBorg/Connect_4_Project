#This class manages everything player related 
class Player:

  '''
  Functions Created:
    add_chip()          - Updates the board with locations of chips for each player.

  '''
  def add_chip(board, row, columns, playerID):
    board[row][columns] = playerID
  
  def player_win(playerID):
    print("Congratulations Player", playerID, "! You Win!")