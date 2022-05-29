# Pieces
from empty import Empty
from pawn import Pawn
from knight import Knight
from rook import Rook
from bishop import Bishop
from queen import Queen
from king import King
# Move
from move import Move
# colored text for console output
from colorama import Fore, Style


class Chess:
    # Chess constructor
    def __init__(self):
        self.board = [[Empty for col in range(8)] for row in range(8)]
        self.fillBoard()
        self.move = Move()
        self.whiteToMove = True

    # the man loop where the game happens
    def gameLoop(self) -> None:
        # loop represents the overall game loop
        while (True):  # input("Would you like to move? (y/n)\n") == "y"

            # GET USER INPUT--------------------------------------------------------------------

            # while loop double checks that the input is valid for chess notation
            # (valid move is checked elsewhere)

            moveInput = input("Please input your move with the following notation: " +
                              "[pieceLocation]-[pieceDestination] (Example: a2-a3)\n")
            if not (len(moveInput) == 5 and (moveInput[0] and moveInput[3]) in "abcdefgh"
                    and (moveInput[1] and moveInput[4]) in "12345678"):
                print(Fore.RED + "Invalid input!" + Style.RESET_ALL)
                continue

            self.move.setMove(moveInput)
            print(f"Your movement of {moveInput} is (Col,Row): " +
                  f" ({self.move.getStartC()},{self.move.getStartR()})" +
                  f" -> ({self.move.getEndC()},{self.move.getEndR()})\n")

            # CHECK USER INPUT IS VALID----------------------------------------------------------
            validMove = False
            if (
                    (self.whiteToMove and self.board[self.move.getStartR()][
                        self.move.getStartC()].getColor() == "white")
                    or
                    (not self.whiteToMove and self.board[self.move.getStartR()][
                        self.move.getStartC()].getColor() == "black")
            ):
                validMove = self.board[self.move.getStartR()][self.move.getStartC()].canMove(self.move, self.board)
            else:
                print(Fore.RED + "Wrong Color!" + Style.RESET_ALL)
            if (not validMove):
                print(Fore.RED + "That was an invalid move, please make a legal move" + Style.RESET_ALL)
            else:
                self.whiteToMove = not self.whiteToMove

            # MAKE THE "MOVE" CHANGE------------------------------------------------------------
            if (validMove):
                self.board[self.move.getEndR()][self.move.getEndC()] = (
                    type(self.board[self.move.getStartR()][self.move.getStartC()])
                    (self.move.getEndR(), self.move.getEndC(),
                     self.board[self.move.getStartR()][self.move.getStartC()].getColor())
                )
                self.board[self.move.getEndR()][self.move.getEndC()].moved()

                self.board[self.move.getStartR()][self.move.getStartC()] = (
                    Empty(self.move.getStartR(), self.move.getStartC(), "n/a")
                )
                # print(f"Color at new square is: {self.board[self.move.getEndR()][self.move.getEndC()].getColor()}")
            # REPEAT------------------------------------------------------------------------------
            print(self.__str__())

    # sets the board up for the beginning of the game
    def fillBoard(self) -> None:
        for row in range(8):
            for col in range(8):
                # all black pieces
                if (row == 0 and (col == 0 or col == 7)):
                    self.board[row][col] = Rook(row, col, "black")
                elif (row == 0 and (col == 1 or col == 6)):
                    self.board[row][col] = Knight(row, col, "black")
                elif (row == 0 and (col == 2 or col == 5)):
                    self.board[row][col] = Bishop(row, col, "black")
                elif (row == 0 and col == 3):
                    self.board[row][col] = Queen(row, col, "black")
                elif (row == 0 and col == 4):
                    self.board[row][col] = King(row, col, "black")
                elif (row == 1):
                    self.board[row][col] = Pawn(row, col, "black")
                # all white pieces
                elif (row == 7 and (col == 0 or col == 7)):
                    self.board[row][col] = Rook(row, col, "white")
                elif (row == 7 and (col == 1 or col == 6)):
                    self.board[row][col] = Knight(row, col, "white")
                elif (row == 7 and (col == 2 or col == 5)):
                    self.board[row][col] = Bishop(row, col, "white")
                elif (row == 7 and col == 3):
                    self.board[row][col] = Queen(row, col, "white")
                elif (row == 7 and col == 4):
                    self.board[row][col] = King(row, col, "white")
                elif (row == 6):
                    self.board[row][col] = Pawn(row, col, "white")
                # all empty squares
                else:
                    self.board[row][col] = Empty(row, col, "n/a")

    # prints out the board
    def __str__(self) -> None:
        print_string = "Chess Board: \n"
        # gets the row in board
        for rowArr in self.board:
            for pieceIndex in range(8):
                # sets the color for the pieces
                if (rowArr[pieceIndex].getColor() == "black"):
                    print_string += Fore.RED
                elif (rowArr[pieceIndex].getColor() == "white"):
                    print_string += Fore.BLUE
                print_string += f"{str(rowArr[pieceIndex])}"
                print_string += Style.RESET_ALL
                if (pieceIndex != 7):
                    print_string += "|"
            if (self.board[7] != rowArr):
                print_string += "\n___ ___ ___ ___ ___ ___ ___ ___\n"
        return print_string
