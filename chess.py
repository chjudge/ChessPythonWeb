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
# Board
from board import Board
# colored text for console output
from colorama import Fore, Style


class Chess:
    # Chess constructor
    def __init__(self):
        self.board = Board()
        self.move = Move()
        self.whiteToMove = True

    # the man loop where the game happens
    def gameLoop(self) -> None:
        # loop represents the overall game loop
        while True:  # input("Would you like to move? (y/n)\n") == "y"

            # GET USER INPUT--------------------------------------------------------------------

            # while loop double checks that the input is valid for chess notation
            # (valid move is checked elsewhere)

            moveInput = input("Please input your move with the following notation: " +
                              "[pieceLocation]-[pieceDestination] (Example: a2-a3)\n").lower()
            move_validate = self.move.setMove(moveInput)
            if move_validate is False:
                print(Fore.RED + "Invalid input!" + Style.RESET_ALL)
                continue

            print(f"Your movement of {moveInput} is (Col,Row): " +
                  f" ({self.move.start_col},{self.move.start_row})" +
                  f" -> ({self.move.end_col},{self.move.end_row})\n")

            # CHECK USER INPUT IS VALID----------------------------------------------------------
            validMove = False
            if (
                    (self.whiteToMove and 
                    self.board.getPiece(self.move.start_row, self.move.start_col).color == "white")
                    or
                    (not self.whiteToMove and 
                    self.board.getPiece(self.move.start_row, self.move.start_col).color == "black")
            ):
                validMove = self.board.getPiece(self.move.start_row,self.move.start_col).canMove(self.move, self.board)
            else:
                print(Fore.RED + "Wrong Color!" + Style.RESET_ALL)
                continue

            # MAKE THE "MOVE" CHANGE------------------------------------------------------------
            if validMove:
                self.board.getPiece(self.move.end_row,self.move.end_col) = (
                    type(self.board.getPiece(self.move.start_row,self.move.start_col))
                    (self.move.end_row, self.move.end_col,
                     self.board.getPiece(self.move.start_row,self.move.start_col).color)
                )
                self.board.getPiece(self.move.end_row,self.move.end_col).moved()

                self.board.getPiece(self.move.start_row,self.move.start_col) = (
                    Empty(self.move.start_row, self.move.start_col, "n/a")
                )
                if isinstance(self.board.getPiece(self.move.end_row,self.move.end_col), King):
                    if self.whiteToMove:
                        self.white_king = self.board.getPiece(self.move.end_row,self.move.end_col)
                    else:
                        self.black_king = self.board.getPiece(self.move.end_row,self.move.end_col)
                self.whiteToMove = not self.whiteToMove
                # print(f"Color at new square is: {self.board.getPiece(self.move.end_row,self.move.end_col).color}")
            else:
                print(Fore.RED + "That was an invalid move, please make a legal move" + Style.RESET_ALL)
            # REPEAT------------------------------------------------------------------------------
            print(self.__str__())

    def in_check(self) -> bool:
        # check if the king is in check
        if self.whiteToMove:
            king = self.white_king
        else:
            king = self.black_king
        for row in range(8):
            for col in range(8):
                if (
                        (self.whiteToMove and self.board[row][col].color == "black")
                        or
                        (not self.whiteToMove and self.board[row][col].color == "white")
                ):
                    if self.board[row][col].canMove(Move(king.row, king.col, row, col), self.board):
                        return True
        return False

    # # sets the board up for the beginning of the game
    # def fillBoard(self) -> None:
    #     for row in range(8):
    #         for col in range(8):
    #             # all black pieces
    #             if (row == 0 and (col == 0 or col == 7)):
    #                 self.board[row][col] = Rook(row, col, "black")
    #             elif (row == 0 and (col == 1 or col == 6)):
    #                 self.board[row][col] = Knight(row, col, "black")
    #             elif (row == 0 and (col == 2 or col == 5)):
    #                 self.board[row][col] = Bishop(row, col, "black")
    #             elif (row == 0 and col == 3):
    #                 self.board[row][col] = Queen(row, col, "black")
    #             elif (row == 0 and col == 4):
    #                 self.board[row][col] = King(row, col, "black")
    #             elif (row == 1):
    #                 self.board[row][col] = Pawn(row, col, "black")
    #             # all white pieces
    #             elif (row == 7 and (col == 0 or col == 7)):
    #                 self.board[row][col] = Rook(row, col, "white")
    #             elif (row == 7 and (col == 1 or col == 6)):
    #                 self.board[row][col] = Knight(row, col, "white")
    #             elif (row == 7 and (col == 2 or col == 5)):
    #                 self.board[row][col] = Bishop(row, col, "white")
    #             elif (row == 7 and col == 3):
    #                 self.board[row][col] = Queen(row, col, "white")
    #             elif (row == 7 and col == 4):
    #                 self.board[row][col] = King(row, col, "white")
    #             elif (row == 6):
    #                 self.board[row][col] = Pawn(row, col, "white")
    #             # all empty squares
    #             else:
    #                 self.board[row][col] = Empty(row, col, "n/a")

    # prints out the board

