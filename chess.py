from piece import Piece 
from empty import Empty
class Chess:
    # Chess constructor
    def __init__(self):
        self.board = [[Piece for col in range(8)] for row in range(8)]
        self.fillBoard()
        print("This is chess")
        # self.__str__()

    def fillBoard(self):
        for row in range(8):
            for col in range(8):
                self.board[row][col] = Empty(row,col, "e")
    
    # prints out the board
    def __str__(self):
        print_string = "toString: \n"
        for arr in self.board:
            for ko in arr:
                print_string += f"{str(ko)}\n"
        return print_string
            # for col in range(8):
                