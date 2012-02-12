# Created by Carson Wilcox for Professor Szpakowicz's AI class CSI 4106
# These 
# Main class runs the game
from board import *
from minmax import *
    
# define auxilary methods
def getUserMove():
    print("Select one of your tokens eg. " + chr(b.whitelist[0][0]+97) + str(b.whitelist[0][1]))
    moveFrom = ""
    while True: # Loop until proper input
        moveFrom = raw_input().strip()
        if not(len(moveFrom) > 0 and len(moveFrom) < 3):
            print ("That is not a valid way of naming your piece, try again (eg. \'a2\')")
        elif (moveFrom == "help" or moveFrom == "Help" or moveFrom == "HELP"):
            print("Select one of your tokens eg. " + chr(b.whitelist[0][0]+97) + str(b.whitelist[0][1]))
        else:
            break
    
    moveFromTup = (int(moveFrom[0]),(int(moveFrom[1])))
    
    print("Select a place you would like to go (eg. e3")
    while True: # Loop until proper input
        moveTo = raw_input().strip()
        if not(len(moveFrom) > 0 and len(moveFrom) < 3):
            print ("That is not a location, try again (eg. \'a2\')")
        elif (moveTo == "help" or moveTo == "Help" or moveTo == "HELP"):
            print("Select a place you would like to go (eg. e3")
        else:
            break
            
    moveToTup = (int(moveTo[0]),(int(moveTo[1])))
    move = (moveFrom, moveTo)
    return move

# Setup the board
print("Input board width")
width = int(raw_input())
print("Input board height")
height = int(raw_input())
print("Enter a number between 0 and 7 for the difficulty setting. 7 = hardest "
    + "0 = dead easy:")
maxDepth = int(raw_input())

b = board(width, height)
b.printBoard()

# Main game loop
while not(b.gameWon):
    print("Welcome to checkers. Type help at any time for additional information")
    # First it is the users turn
    userMove = getUserMove()
    print userMove
    break
    # Then it is the computers turn
    # minmax(b, maxDepth)
    # TODO
    
#Print the list of tokens
#print "Blacklist:\n"
#for piece in b.blacklist:
#    print str(piece[0]) + " , " + str(piece[1]) + "\n"
#print "Whitelist:\n"
#for piece in b.whitelist:
#    print str(piece[0]) + " , " + str(piece[1]) + "\n"
