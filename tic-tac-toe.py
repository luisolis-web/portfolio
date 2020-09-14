#! /usr/bin/env
from __future__ import print_function
print('Tic-Tac-Toe\n\n')
prevMoves = []
# The board is composed of lists
board = [[' ','|',' ','|',' '],['-','+','-','+','-'],[' ','|',' ','|',' '],['-','+','-','+','-'],[' ','|',' ','|',' ']]


def printBoard():
    for i in board:
        for x in i:
            print(x,end="") # I print the board every attempted turn
        print()

def getPlayer():
    if len(prevMoves)%2 == 0: # This ensures the first player is 'x', and that it swaps every successful turn
        player = 'x'
    else:
        player = 'o'
    return player

def getEntry(): # Gets the user's entry and writes it to the board
    player = getPlayer()

    row = 0 # These two while statements take only an int input
    while row < 1 or row > 3:
        row = int(input('Row(1-3):    '))
    print()
    column = 0
    while column < 1 or column > 3:
        column = int(input('Column(1-3): '))

    # Lines 32-44 convert the input into their corresponding indexes
    if row == 1:
        row = 0
    elif row == 2:
        row = 2
    elif row == 3:
        row = 4

    if column == 1:
        column = 0
    elif column == 2:
        column = 2
    elif column == 3:
        column = 4 
    # The rest of the function determines whether the chosen spot has been taken yet, and prints if so
    taken = False
    i = 0
    while taken == False and i < len(prevMoves): # Terms to exit require the spot be taken,
                                                 # or the index have exceeded the list
        if prevMoves[i] == [row,column]:
            print('That spot is already taken. Please try again')
            taken = True
        i += 1
    # If the spot is available, the player will be written to the board, and the move will be logged
    if taken == False:
        prevMoves.append([row,column])
        board[row][column] = player
    # Hello there
    print()


def getWinner():
    # Determines the winner or lack thereof
    player = getPlayer()
    if player == 'x':
        player = 'o'
    else:
        player = 'x'
    if board[0][0] == player and board[0][2] == player and board[0][4] == player:
        return player
    elif board[2][0] == player and board[2][2] == player and board[2][4] == player:
        return player
    elif board[4][0] == player and board[4][2] == player and board[4][4] == player:
        return player
    elif board[0][0] == player and board[2][0] == player and board[4][0] == player:
        return player
    elif board[0][2] == player and board[2][2] == player and board[4][2] == player:
        return player
    elif board[0][4] == player and board[2][4] == player and board[4][4] == player:
        return player
    elif board[0][0] == player and board[2][2] == player and board[4][4] == player:
        return player
    elif board[4][0] == player and board[2][2] == player and board[0][4] == player:
        return player
        
    print()
    return 'nobody'


def main():
    i = -1
    while getWinner() == 'nobody' and len(prevMoves) < 9:
        #player = getPlayer()
        i += 1
        printBoard()
        getEntry()
        getWinner()

    printBoard()
    print(getWinner(),'wins!')
    input('ENTER to exit: ')

if __name__ == '__main__':
    main()
