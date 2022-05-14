
class Move():
    def __init__(self):
        self.startPosR = None
        self.startPosC = None
        self.endPosR = None
        self.endPosC = None

# Setter Method
    def setMove(self, sPR, sPC, ePR, ePC):
        self.startPosR = sPR
        self.startPosC = sPC
        self.endPosR = ePR
        self.endPosC = ePC

# Getter Methods
    def getStartR(self):
        return self.startPosR
    def getStartC(self):
        return self.startPosC
    def getEndR(self):
        return self.endPosR
    def getEndC(self):
        return self.endPosC

    

    print("HI")
