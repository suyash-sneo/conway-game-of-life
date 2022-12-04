from Constants import *
from Utils import Utils

class GameOfLife:

    def __init__(self):
        self.Board = Utils.GetInitialBoardConfig()

    def getBoard(self):
        return self.Board

    def changeCellState(self, row, col):
        self.Board[row][col] = 1 - self.Board[row][col]

    def updateToNextStep(self):
        tempBoard = Utils.GetEmptyBoardConfig()

        for row in range(1, NUM_OF_ROWS-1):
            for col in range(1, NUM_OF_COLUMNS-1):
                numOfNeighbours = self.getNeighboursCountAtIndex(row, col)
                if (self.Board[row][col]==1) and (numOfNeighbours==2 or numOfNeighbours==3):
                    tempBoard[row][col]=1
                elif (self.Board[row][col]==0) and (numOfNeighbours==3):
                    tempBoard[row][col]=1

        self.Board = tempBoard
        return self.Board

    def getNeighboursCountAtIndex(self, row, col):
        numOfNeighbours = 0
        
        if self.Board[row-1][col-1] == 1:
            numOfNeighbours += 1
        if self.Board[row-1][col] == 1:
            numOfNeighbours += 1
        if self.Board[row-1][col+1] == 1:
            numOfNeighbours += 1
        if self.Board[row][col-1] == 1:
            numOfNeighbours += 1
        if self.Board[row][col+1] == 1:
            numOfNeighbours += 1
        if self.Board[row+1][col-1] == 1:
            numOfNeighbours += 1
        if self.Board[row+1][col] == 1:
            numOfNeighbours += 1
        if self.Board[row+1][col+1] == 1:
            numOfNeighbours += 1

        return numOfNeighbours