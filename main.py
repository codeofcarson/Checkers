# Created by Carson Wilcox for Professor Szpakowicz's AI class CSI 4106
# These 
# Main class runs the game
from board import *
from minmax import *

# Setup variables
width = 6
height = 6
firstPlayer = 0

# Gets the move from the User
def getUserMove(b):
    statement1 = "Select one of your tokens eg. " + chr(b.whitelist[0][0]+97) + str(b.whitelist[0][1])
    print(statement1)
    while True: # Loop until proper input
        move = []
        move = raw_input().lower().split()
        if not(len(move) == 2):
            print "That is not a valid move, try again.", statement1
            continue
        moveFromTup = (int(move[0][1]), ord(move[0][0]) - 97)
        moveToTup = (int(move[1][1]), ord(move[1][0]) - 97)
        # Is the piece we want to move one we own?
        if not (moveFromTup in b.whitelist):
            print "You do not own", moveFromTup, "please select one of.", b.whitelist
            continue
        break
    move = (moveFromTup, moveToTup, b.NOTDONE)
    return move

### MAIN PROGRAM ###

b = board(width, height, firstPlayer)
b.printBoard()
print("Welcome to checkers.")

# Main game loop
while b.gameWon == -1:
    # First it is the users turn
    userMove = getUserMove(b)
    try:
        b.moveWhite(*userMove)
    except Exception:
        print "Invalid move"
        continue
        
    # Then it is the computers turn
    temp = minMax2(b)
    b = temp[0]
    print "**********COMPUTER MOVE**********"
    b.printBoard()
    if b.gameWon == b.WHITE:
        print "White Wins\nGame Over"
        break
    elif b.gameWon == b.BLACK:
        print "Black Wins\nGame Over"
        break
