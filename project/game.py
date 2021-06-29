from board import Board
import time, sys

class Game():
    def __init__(self, readFile, writeFile):
        self.board = Board(filename=readFile)
        self.readFile = readFile
        self.writeFile = writeFile
    
    def step(self):
        self.board.updateBoard()

def main():
    game = Game('layout', 'output')
    if len(sys.argv) == 1:
        print('usage: python(3) game.py <option>')
        print('OPTIONS: step  - iterate one at a time on user input')
        print('         clock - iterate based on ingame clock')
        exit(1)
    if sys.argv[1].upper() == 'STEP':
        while True:
            print(game.board)
            input('next Step? (Y:any)')
            game.step()
    elif sys.argv[1].upper() == 'CLOCK':
        while True:
            print(game.board)
            time.sleep(0.1)
            game.step()
    else:
        print('usage: python(3) game.py <option>')
        print('OPTIONS: step  - iterate one at a time on user input')
        print('         clock - iterate based on ingame clock')
        exit(1)
if __name__ == '__main__':
    main()