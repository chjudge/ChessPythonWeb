# from piece import Piece 
from empty import Empty
from pawn import Pawn
from knight import Knight
from rook import Rook
from bishop import Bishop
from queen import Queen
from king import King
# colored text for console output
from colorama import Fore, Style
class Chess:
    # Chess constructor
    def __init__(self):
        self.board = [[Empty for col in range(8)] for row in range(8)]
        self.fillBoard()
        print("This is chess")
        # self.__str__()

    def fillBoard(self):
        for row in range(8):
            for col in range(8):
                # all black pieces
                if(row == 0 and (col == 0 or col == 7)):  
                    self.board[row][col] = Rook(row,col,"black")
                elif(row == 0 and (col == 1 or col == 6)):
                    self.board[row][col] = Knight(row, col,"black")
                elif(row == 0 and (col == 2 or col == 5)):
                    self.board[row][col] = Bishop(row, col,"black")
                elif(row == 0 and col == 3):
                    self.board[row][col] = Queen(row, col,"black")
                elif(row == 0 and col == 4):
                    self.board[row][col] = King(row, col,"black")
                elif(row == 1):
                    self.board[row][col] = Pawn(row, col,"black")
                # all white pieces
                elif(row == 7 and (col == 0 or col == 7)):  
                    self.board[row][col] = Rook(row,col,"white")
                elif(row == 7 and (col == 1 or col == 6)):
                    self.board[row][col] = Knight(row, col,"white")
                elif(row == 7 and (col == 2 or col == 5)):
                    self.board[row][col] = Bishop(row, col,"white")
                elif(row == 7 and col == 3):
                    self.board[row][col] = Queen(row, col,"white")
                elif(row == 7 and col == 4):
                    self.board[row][col] = King(row, col,"white")
                elif(row == 6):
                    self.board[row][col] = Pawn(row, col,"white")
                # all empty squares
                else:
                    self.board[row][col] = Empty(row,col,"n/a")
    
    # prints out the board
    def __str__(self):
        print_string = "Chess Board: \n"
        #gets the row in board
        for rowArr in self.board:
            # print_string += "["
            for pieceIndex in range(8):
                # sets the color for the pieces
                if(rowArr[pieceIndex].getColor() == "black"):
                    print_string += Fore.RED
                elif(rowArr[pieceIndex].getColor() == "white"):
                    print_string += Fore.BLUE
                print_string += f"{str(rowArr[pieceIndex])}"
                print_string += Style.RESET_ALL
                if(pieceIndex != 7):
                    print_string += "|"
            if(self.board[7] != rowArr):
                print_string += "\n___ ___ ___ ___ ___ ___ ___ ___\n"
        return print_string
                