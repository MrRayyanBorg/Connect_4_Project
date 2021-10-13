import numpy as np

class Board:
  def __init__(self):
    pass

  def create2dArray(self,vertical,horizontal):
    vertical_array   = []
    horizontal_array = []
    for i in range(0,horizontal):
      horizontal_array.append(0)
    for i in range(0,vertical):
      vertical_array.append(horizontal_array)
    return vertical_array

  def formatArray(self,array):
    for item in array:
      print(item)
  
  #this function creates a board along an x,y
  def create_board(self,rows,columns):
    self.board = self.create2dArray(rows,columns) #creates board 6 by 7
    return self.board

  #this function outputs the board on a flipped axis
  def print_board(self):
    self.formatArray(self.board)

  def get_next_open_row(self, rows, input_column):
  #this function checks which row is not taken, closest to the first row and within input column
    #print(rows[input_column])
    for i in range(rows):
      if self.board[i][input_column] == 0:
        return i
    
        
        