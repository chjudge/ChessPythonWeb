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
#GUI


class Chess:
    # Chess constructor
    def __init__(self):
        self.board = Board()
        self.move = Move()
        self.whiteToMove = True
        self.castling = False

    # the man loop where the game happens
    def gameLoop(self) -> None:
        # loop represents the overall game loop
        while True:  # input("Would you like to move? (y/n)\n") == "y"

            # GET USER INPUT--------------------------------------------------------------------

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
                self.board.setUndo(self.move)

            else:
                print(Fore.RED + "Wrong Color!" + Style.RESET_ALL)
                continue

            # MAKE THE "MOVE" CHANGE------------------------------------------------------------
            if validMove:
                self.board.movePiece(self.move, len(self.board.en_passant) != 0)

                if(self.whiteToMove):
                    validMove = not self.board.white_pieces[4].kingCheck(
                        self.board.white_pieces[4].row, self.board.white_pieces[4].col, self.board)
                else:
                    validMove = not self.board.black_pieces[4].kingCheck(
                        self.board.black_pieces[4].row, self.board.black_pieces[4].col, self.board)
                if(validMove): 
                    # resets en Passant values
                    if(len(self.board.en_passant) != 0):
                        if((self.whiteToMove and self.board.en_passant[0].color == "white") or
                            (not self.whiteToMove and self.board.en_passant[0].color == "black")):
                            self.board.en_passant.clear()
                    self.whiteToMove = not self.whiteToMove
                else:
                    self.board.undo(len(self.board.en_passant) != 0)
                    print(Fore.RED + "King is in Check!" + Style.RESET_ALL)
            else:
                print(Fore.RED + "That was an invalid move, please make a legal move" + Style.RESET_ALL)

            # undoes the move if it was illegal
                if(validMove):
                    if(self.whiteToMove):
                        validMove = not self.board.white_pieces[4].kingCheck(
                            self.board.white_pieces[4].row, self.board.white_pieces[4].col, self.board)
                    else:
                        validMove = not self.board.black_pieces[4].kingCheck(
                            self.board.black_pieces[4].row, self.board.black_pieces[4].col, self.board)


            # REPEAT------------------------------------------------------------------------------
            print(self.board.__str__())

