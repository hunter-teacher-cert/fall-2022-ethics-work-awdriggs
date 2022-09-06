# gol.py
# Adam Driggers
# CSCI 77800 Fall 2022
# collaborators:
# consulted:

# importing the necessary packages
import time #for delay
import os #for clearing terminal window for animation
import random as r

# build the game board
def buildBoard(numRows, numCols):
    board = []
    for x in range(numRows):
        row = []
        for y in range(numCols):
            # row.append(0) #0 for dead cells
            row.append(randomState()) # randomly assign alive or dead 
        board.append(row)

    # print(board) #for debug
    return board
 
def randomState():
    v = r.random()
    prob = 0.8 

    if(v > prob):
        return 1
    else:
        return 0

# print the game board to the screen, pretty like
def printBoard(board):
    alive = "\U0001F7E9"
    dead = "\U0001F7E6"

    for row in board:
        rowString = ""
        for col in row:
            if col == 0:
                rowString += dead
            else:
                rowString += alive

        print(rowString)

# set an individual cell
def setCell(b, r, c, v):
    b[r][c] = v

# count the neighbor for each cell
def countNeighbors(b, r, c):
    count = 0

    for i in range(r-1, r+2, 1):
        for j in range(c-1, c+2, 1):
            # print("row %s col %s" % (i, j))
            # print(not(i == r and j == c))

            # only check a valid index and don't cound yourself
            if validIndex(b, i, j) and not(i == r and j == c):
                # print(b[i][j])
                count += b[i][j] #since 0 is dead and 1 is alive, just count your neighbors

    return count



# valid index check
def validIndex(l, r, c):
    if 0<= r < len(l) and 0 <= c < len(l[r]):  #only check positive indices
        try: #see if this is a valid index, return true if yes, false if no
            l[r][c]
            return True
        except IndexError:
            return False
    else:
        return False #negative index, alwasy return false

def getNextCell(l, r, c):
    nextValue = l[r][c] #start with the current value
    count = countNeighbors(l, r, c)

    if nextValue:
        if count < 2 or count > 3:
            nextValue = 0
    else:
        if count == 3:
            nextValue = 1

    return nextValue

def getNextBoard(l):
    nextBoard = [x[:] for x in l] #copy the 2d array, help from stack overflow

    for r in range(len(l)):
        for c in range(len(l[r])):
            nextBoard[r][c] = getNextCell(l, r, c)

    return nextBoard

# clear the terminal window
def clear():
    # for windows OS
    if os.name =="nt":
        os.system("cls")
    else:# for linux / Mac OS
        os.system("clear")

# main program loop

board = buildBoard(50, 50) #build the initial board

# create a random board


#board[1][1] = 1 #testing out the printing
#board[1][2] = 1 #testing out the printing
#board[1][3] = 1 #testing out the printing
#board[2][1] = 1 #testing out the printing
#board[2][3] = 1 #testing out the printing
#board[3][1] = 1 #testing out the printing
#board[3][2] = 1 #testing out the printing
#board[3][3] = 1 #testing out the printing

#copy = [x[:] for x in board] #copy a board help from stack overflow

# print(board) #prints a ugly board using 1s, 0s
clear()

while True:
    printBoard(board) #prints a pretty board using emoji
    board = getNextBoard(board)
    time.sleep(1)
    clear()

# print("-------------------------------------------")
# printBoard(copy)

# test checking for valid indexes
# print(validIndex(board, 1, 1))
# print(validIndex(board, 10, 10))
# print(validIndex(board, -1, -1))
# print(validIndex(board, 9, 8))

# testing coutning the neighbors
# print(countNeighbors(board, 2, 2))
# print(countNeighbors(board, 3, 3))

# test getting the next cell value
# print(getNextCell(board, 0, 2))
# print(getNextCell(board, 2, 2))
# print(getNextCell(board, 4, 2))
#


# print("\U00002B1B1") #black square
# print("\U0001F7E9")
# print("\U0001F7E6")

# testing animation
# while frame < 100:
#     print(frame)
#     time.sleep(1)
#     clear()
#     frame += 1

