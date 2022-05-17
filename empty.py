from piece import Piece as p

class Empty(p):
    # Constuctor defined in parents
    # def __init__(self, xpos, ypos, color):
    #     p.__init__(self, xpos, ypos, color)
    def toString(self):
        print("hi")
        return "EMPTY SPACE"