import numpy as np
from random import randint
from math import sqrt

class SolitairBoard():

    def __init__(self):
        self.board = np.ones((7,7))
        self.board[3][3] = 0
        self.pastMoves = []

        for i in range(4):
            self.board[1][0] = -1
            self.board[0][0] = -1
            self.board[1][1] = -1
            self.board[0][1] = -1
            self.board = np.rot90(self.board)

    def __str__(self):
        return str(self.board)
    
    def getLegalMoves(self):
        emptyPins = list(zip(np.where(self.board==0)[0], np.where(self.board==0)[1]))
        moves = []
        for noPin in emptyPins:
            for direc in range(-1, 2, 2):
                if self.isPin(noPin[0] + direc, noPin[1]) and self.isPin(noPin[0]+ 2*direc, noPin[1]):
                    moves.append((('x', direc), noPin))
                if self.isPin(noPin[0], noPin[1] + direc) and self.isPin(noPin[0], noPin[1]+ 2*direc):
                    moves.append((('y', direc), noPin))
        return moves 

    def isPin(self, x, y):
        return self.isOnBoard(x, y) and self.board[x][y] == 1
    
    def isOnBoard(self, x, y):
        return not (x < 0 or x > 6 or y < 0 or y > 6 or self.board[x][y] == -1)
    
    def updateBoard(self, move):
        self.pastMoves.append(move)
        direc = move[0][1]
        self.board[move[1][0]][move[1][1]] = 1
        for i in range(1,3):
            if move[0][0] == 'x':
                self.board[move[1][0] + direc * i][move[1][1]] = 0
            if move[0][0] == 'y':
                self.board[move[1][0] ][move[1][1]+ direc * i] = 0
        

    def score(self):
        return 33 - np.count_nonzero(self.board == 1)
    
    def reward(self):
        reward = 1.1** self.score()
        pins = list(zip(np.where(self.board==1)[0], np.where(self.board==1)[1]))
        totalDistanceSum = 0
        for pin in pins:
            totalDistanceSum += sqrt(abs(pin[0] - 3)**2 + abs(pin[1] - 3)**2)

        avg = totalDistanceSum / len(pins)
        reward += 2 * (4 - avg)
        return reward 



minScore = 30
minBoard = None
board = SolitairBoard()
print(board.score())
for i in range(1):
    print(str(i/100), end="\r")
    board = SolitairBoard()
    moves = board.getLegalMoves()
    while len(moves) > 0:
        ind = randint(0, len(moves)- 1)
        board.updateBoard(moves[ind])
        moves = board.getLegalMoves()
    if board.score() < minScore:
        minBoard = board
        minScore = board.score()
print(minScore)
print(minBoard.pastMoves)
print(minBoard)
print(minBoard.reward())

# twoLast = "[(('x', -1), (3, 3)), (('y', -1), (2, 3)), (('x', 1), (1, 3)), (('x', 1), (3, 3)), (('y', 1), (2, 3)), (('y', 1), (4, 3)), (('x', -1), (2, 4)), (('x', 1), (1, 4)), (('x', 1), (4, 4)), (('x', -1), (2, 2)), (('x', -1), (5, 3)), (('x', 1), (4, 3)), (('y', -1), (3, 3)), (('y', 1), (3, 4)), (('y', -1), (3, 5)), (('y', 1), (2, 1)), (('x', -1), (2, 3)), (('y', -1), (2, 2)), (('x', 1), (3, 2)), (('y', 1), (2, 1)), (('x', 1), (2, 0)), (('y', -1), (4, 5)), (('y', 1), (4, 4)), (('y', -1), (2, 2)), (('x', -1), (4, 2)), (('y', -1), (4, 3)), (('y', -1), (4, 5)), (('x', 1), (2, 5)), (('y', 1), (2, 4)), (('x', 1), (0, 4))]"
