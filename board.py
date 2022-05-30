from colorama import Fore, Style

from empty import Empty
from pawn import Pawn
from knight import Knight
from rook import Rook
from bishop import Bishop
from queen import Queen
from king import King


class Board:
    def __init__(self):
        self.white_pieces = []
        self.black_pieces = []
        self.board = []
        self.create_board()

    def create_board(self):
        self.board = [[Empty for col in range(8)] for row in range(8)]

        self.white_pieces.append(Rook(0, 7, "white"))
        self.white_pieces.append(Knight(1, 7, "white"))
        self.white_pieces.append(Bishop(2, 7, "white"))
        self.white_pieces.append(Queen(3, 7, "white"))
        self.white_pieces.append(King(4, 7, "white"))
        self.white_pieces.append(Bishop(5, 7, "white"))
        self.white_pieces.append(Knight(6, 7, "white"))
        self.white_pieces.append(Rook(7, 7, "white"))
        for i in range(8):
            self.white_pieces.append(Pawn(i, 6, "white"))

        for p in self.white_pieces:
            self.board[p.row][p.col] = p

        self.black_pieces.append(Rook(0, 0, "black"))
        self.black_pieces.append(Knight(1, 0, "black"))
        self.black_pieces.append(Bishop(2, 0, "black"))
        self.black_pieces.append(Queen(3, 0, "black"))
        self.black_pieces.append(King(4, 0, "black"))
        self.black_pieces.append(Bishop(5, 0, "black"))
        self.black_pieces.append(Knight(6, 0, "black"))
        self.black_pieces.append(Rook(7, 0, "black"))
        for i in range(8):
            self.black_pieces.append(Pawn(i, 1, "black"))

        for p in self.black_pieces:
            self.board[p.row][p.col] = p

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