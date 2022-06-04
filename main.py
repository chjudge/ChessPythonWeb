from chess import Chess

def main():
    chess = Chess()
    print(chess.board.__str__())
    
    chess.gameLoop()
    print("Program Complete")

if __name__=='__main__':
    main()
