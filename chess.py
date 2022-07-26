# Move
from move import Move
# Board
from board import Board
# colored text for console output
from colorama import Fore, Style


# GUI


class Chess:
    # Chess constructor
    def __init__(self):
        self.board = Board()
        self.move = Move()
        self.whiteToMove = True

    # the main loop where the game happens
    def game_loop(self) -> None:
        # loop represents the overall game loop
        while True:  # input("Would you like to move? (y/n)\n") == "y"

            # GET USER INPUT--------------------------------------------------------------------

            move_input = input("Please input your move with the following notation: " +
                               "[pieceLocation]-[pieceDestination] (Example: a2-a3)\n").strip().lower()
            
            if self.move.set_move(move_input) is False:
                print(Fore.RED + "Invalid input!" + Style.RESET_ALL)
                continue

            # print(f"Your movement of {move_input} is (Col,Row): " +
            #       f" ({self.move.start_col},{self.move.start_row})" +
            #       f" -> ({self.move.end_col},{self.move.end_row})\n")

            piece = self.board.get_piece(self.move.start_row, self.move.start_col)

            # CHECK USER INPUT IS VALID----------------------------------------------------------
            # check if the piece is the player's color
            if (self.whiteToMove and piece.color == "black") or (self.whiteToMove is False and piece.color == "white"):
                print(Fore.RED + "Wrong Color!" + Style.RESET_ALL)
                continue

            self.board.set_undo(self.move)

            # Check if the piece can move to the end location
            if not piece.can_move(self.move, self.board):
                print(Fore.RED + "That was an invalid move, please make a legal move" + Style.RESET_ALL)
                continue

            # MAKE THE "MOVE" CHANGE------------------------------------------------------------
            success = self.board.move_piece(self.move, self.whiteToMove)

            if success is False:
                print(Fore.RED + "King is in Check!" + Style.RESET_ALL)
                continue

            # REPEAT------------------------------------------------------------------------------
            # change players turn
            self.whiteToMove = not self.whiteToMove
            print(self.board.__str__())
