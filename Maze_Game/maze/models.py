import random

# Create your models here.
class Block():
    def __init__(self, row, col):
        self.row = row
        self.col = col

    visited = "U"
    movableDirections = ('T','L','R', 'B')
    outSpot = ()
    inSpot = "N"
    treasure = False


class Maze():
    
    def __init__(self, rows, col, difficulty):
        self.rows = rows
        self.col = col
        self.mazeBlock = []
        self.difficulty = difficulty
    
    
    def TraverseMaze(self, blockToMove, positionToMove):
        positions = [[-1, 0], [0, -1], [0, 1], [1, 0]]
        blockToMove.visited = "V"
        if positionToMove == "T":
            movement = positions[0]
            positionsToStep = "B"
        elif positionToMove == "L":
            movement = positions[1]
            positionsToStep = "R"
        elif positionToMove == "R":
            movement = positions[2]
            positionsToStep = "L"
        elif positionToMove == "B":
            movement = positions[3]
            positionsToStep = "T"

        row = blockToMove.row + movement[0]
        col = blockToMove.col + movement[1]
        nextBlock = self.mazeBlock[row][col]
        lastBlock = nextBlock

        if nextBlock.visited != "V":
            oldDirections = list(nextBlock.movableDirections)
            oldDirections.remove(positionsToStep)
            nextBlock.movableDirections = tuple(oldDirections)
            nextBlock.inSpot = positionsToStep

            moveSpots = list(blockToMove.outSpot)
            moveSpots.append(positionToMove)
            blockToMove.outSpot = tuple(moveSpots) 

        if len(nextBlock.movableDirections) != 0:
            newDirections = list(blockToMove.movableDirections)
            newDirections.remove(positionToMove)
            blockToMove.movableDirections = tuple(newDirections)
            positionToMove = random.choice(nextBlock.movableDirections)
            lastBlock = self.TraverseMaze(nextBlock, positionToMove)
            if len(blockToMove.movableDirections) != 0:
                positionToMove = random.choice(blockToMove.movableDirections)
                self.TraverseMaze(blockToMove, positionToMove)
        
        return lastBlock      
            
    def createMaze(self):
        for i in range(self.rows):
            newRow = []
            for j in range(self.col):
               
                newBlock = Block(i, j)
                if i == 0:
                    if j == 0:
                        newBlock.movableDirections = ('R', 'B')
                    
                    elif j == self.col - 1:
                        newBlock.movableDirections = ('L', 'B')
                    
                    else: 
                        newBlock.movableDirections = ('L', 'R', 'B')


                elif i == self.rows - 1:
                    if j == 0:
                        newBlock.movableDirections = ('T', 'R')
                    
                    elif j == self.col - 1:
                        newBlock.movableDirections = ('T', 'L')
                    
                    else: 
                        newBlock.movableDirections = ('T', 'L', 'R')

                else:
                    if j == 0:
                        newBlock.movableDirections = ('T', 'R', 'B')
                    
                    elif j ==  self.col - 1:
                        newBlock.movableDirections = ('T', 'L', 'B')
               
                newRow.append(newBlock)
            
            self.mazeBlock.append(newRow)

        startingCol = random.choice(range(self.col))
        startingRow = random.choice(range(self.rows))
    
        blockToMove = self.mazeBlock[startingRow][startingCol]
        positionToMove = random.choice(blockToMove.movableDirections)
        lastPositions = self.TraverseMaze(blockToMove, positionToMove)

        availableTreasures = self.difficulty
        while availableTreasures > 0:
            treasureCol = random.choice(range(self.col))
            treasureRow = random.choice(range(self.rows))
            if (blockToMove.col != treasureCol and blockToMove.row != treasureRow) and (lastPositions.col != treasureCol and lastPositions.row != treasureRow) and (self.mazeBlock[treasureRow][treasureCol].treasure != True):
                self.mazeBlock[treasureRow][treasureCol].treasure = True
                availableTreasures = availableTreasures - 1

        blockToMove.visited = "POS"
        lastPositions.visited = "END"
        return self.mazeBlock
        
       
        
