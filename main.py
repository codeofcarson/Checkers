# Created by Carson Wilcox for Professor Szpakowicz's AI class CSI 4106
# These 
# Main class runs the game
from board import *
# Setup the board
print("Input board width")
width = int(raw_input())
print("Input board height")
height = int(raw_input())

b = board(width, height)
b.printBoard()

# Main game loop
#while not(b.isWon):
    #TODO do stuff, fuck bitches
#    pass
    
#Print the list of tokens
#print "Blacklist:\n"
#for piece in b.blacklist:
#    print str(piece[0]) + " , " + str(piece[1]) + "\n"
#print "Whitelist:\n"
#for piece in b.whitelist:
#    print str(piece[0]) + " , " + str(piece[1]) + "\n"

