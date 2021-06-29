import copy
HEIGHT = 50
WIDTH = 50

ALIVE = 1
DEAD = 0

class Board():
    def __init__(self, filename=None):
        self.height = HEIGHT
        self.width = WIDTH
        self.board = []
        for i in range(self.height):
            l = []
            for j in range(self.width):
                l.append(DEAD)
            self.board.append(l)
        if filename:
            self.load(filename)
    def r(self):
        msg = str()
        for row in self.board:
            for item in row:
                if item == ALIVE:
                    msg += '#'
                if item == DEAD:
                    msg += '_'
            msg += '\n'
        return msg
    def __repr__(self):
        return self.r()

    def load(self, filename):
        i = 0
        with open(filename, 'r') as f:
            r = f.readlines()
        if len(r) > self.height:
            raise Exception
        for line in r:
            if line == '':
                continue
            l = []
            for item in line:
                if item == '_':
                    l.append(DEAD)
                if item == '#':
                    l.append(ALIVE)
            self.board[i] = l
            i += 1
        f.close()
    
    def output(self, filename='output'):
        with open(filename, 'w') as f:
            list = self.r().split('\n')
            for line in list:
                if line.strip() != '':
                    f.write(line + '\n')
            f.close()
    def getAlive(self, cell):
        '''
            Return the number of living cells around a given cell (i,j)
        '''
        count = 0
        assert isinstance(cell, tuple)
        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):
                # Ignore the cell itself
                if (i, j) == cell:
                    continue
                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j] == ALIVE:
                        count += 1
        return count
    @staticmethod
    def getSurroundings(self, cell):
        assert isinstance(cell, tuple)
        surroundings = set()
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):
                if (i,j) == cell:
                    continue
                if 0 <= i < self.height and 0 <= j < self.width:
                    surroundings.add((i,j))
        return surroundings

    def updateBoard(self):
        '''Update cell based on the rules'''
        '''
            - Any live cell with fewer than two live neighbours dies, as if by underpopulation.
            - Any live cell with two or three live neighbours lives on to the next generation.
            - Any live cell with more than three live neighbours dies, as if by overpopulation.
            - Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
        ''' 
        nextBoard = copy.deepcopy(self.board)
        for i in range(self.height):
            for j in range(self.width):
                cell = (i,j)
                if self.board[i][j] == ALIVE:
                    if self.getAlive(cell) < 2 or self.getAlive(cell) > 3:
                        nextBoard[i][j] = DEAD
                if self.board[i][j] == DEAD:
                    if self.getAlive(cell) == 3:
                        nextBoard[i][j] = ALIVE
        self.board = nextBoard
