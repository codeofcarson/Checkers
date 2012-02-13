# Created by Carson Wilcox for Professor Szpakowicz's AI class CSI 4106
# These 
# Main class runs the game
from board import *
from minmaxSAM import *

# define auxilary methods
# Gets the move from the User
def getUserMove():
    statement1 = "Select one of your tokens eg. " + chr(b.whitelist[0][0]+97) + str(b.whitelist[0][1])
    print(statement1)
    moveFrom = ""
    while True: # Loop until proper input
        moveFrom = raw_input().strip().lower()
        if moveFrom == 'help':
            print(statement1)
        elif not(len(moveFrom) == 2):
            print "That is not a valid way of naming a piece, try again (eg. \'a2\')"
        elif not((int(moveFrom[1]), ord(moveFrom[0]) - 97) in b.whitelist):
            print "You do not own that piece"
        else:
            break
    
    moveFromTup = (int(moveFrom[1]), ord(moveFrom[0]) - 97)
    
    print("Select a place you would like to go (eg. e3)")
    while True: # Loop until proper input
        moveTo = raw_input().strip().lower()
        if moveTo == 'help':
            print("Select a place you would like to go (eg. e3)")
        elif not(len(moveTo) == 2):
            print ("That is not a location, try again (eg. \'a2\')")
        else:
            break
            
    moveToTup = (int(moveTo[1]), ord(moveTo[0]) - 97)
    
    move = (moveFromTup, moveToTup, -1)
    return move

### MAIN PROGRAM ###
# Setup the board
#print("Input board width")
#width = int(raw_input())
#print("Input board height")
#height = int(raw_input())
#print("Enter a number between 0 and 7 for the difficulty setting. 7 = hardest "
#    + "0 = dead easy:")
#maxDepth = int(raw_input())
width = 6
height = 6
maxDepth = 5

b = board(width, height)
mm = Minimax(b)
b.printBoard()
print("Welcome to checkers. Type help at any time for additional information")

# Main game loop
while b.gameWon == -1:
    # First it is the users turn
    userMove = getUserMove()
    b.moveWhite(*userMove)
    # Then it is the computers turn
    temp = mm.minimax()
    b = temp[0].board
#    print b
    print "**********COMPUTER MOVE**********"
    print "best move was", temp[1]
    b.printBoard()
    if b.gameWon == b.WHITE:
        print "White Wins\nGame Over"
        break
    elif b.gameWon == b.BLACK:
        print "Black Wins\nGame Over"
        break
    
#Print the list of tokens
#print "Blacklist:\n"
#for piece in b.blacklist:
#    print str(piece[0]) + " , " + str(piece[1]) + "\n"
#print "Whitelist:\n"
#for piece in b.whitelist:
#    print str(piece[0]) + " , " + str(piece[1]) + "\n"
