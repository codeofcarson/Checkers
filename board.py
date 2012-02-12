# coding: utf-8
# Game board. It needs a height and a width in order
# to be instantiated
class board:
    def __init__(self, height, width):
        # Set the height and width of the game board
        self.width = width
        self.height = height
        # Create two lists which will contain the pieces each player posesses
        self.blacklist = []
        self.whitelist = []
        # Set default piece positions
        for i in range(width):
            self.blacklist.append((i, (i+1)%2))
            self.whitelist.append((i, height - (i%2) - 1))
        # boardState contains the current state of the board for printing/eval
        self.boardState = [[' '] * self.width for x in range(self.height)]
        self.gameWon = False
        self.WHITE = 0
        self.BLACK = 1
        self.turn = self.WHITE
        
    
    # Returns True if there is a piece at that position 
    def contains(self, x, y):
        if ((x,y) in self.blacklist):
            # testing return "Black piece is at " + str(x) +","+ str(y)
            return True
        elif ((x,y) in self.whitelist):
            # testing return "White piece is at " + str(x) +","+ str(y)
            return True
        else:
            # testing return "No piece at " + str(x) +","+ str(y)
            return False
    
    # Generate ALL OF THE MOVES
    def iterWhiteMoves(self):
        for piece in self.whitelist:
            for move in self.iterWhitePiece(piece):
                yield move
                
    def iterBlackMoves(self):
        for piece in self.blacklist:
            #print piece
            for move in self.iterBlackPiece(piece):
                #print move
                yield move
        
    # Creates an iterable list of moves for a white piece
    def iterWhitePiece(self, piece):
        # White pieces can only move up the board
        possibleMove1 = (piece[0]+1, piece[1]-1)
        possibleMove2 = (piece[0]-1, piece[1]-1)
        for move in (possibleMove1, possibleMove2):
            # The move must not go outside the bounds of the board or move to 
            # a location where another piece is already located
            if ((move[0] > -1 and move[0] < self.width) 
            and (move[1] > -1 and move[1] < self.height)
            and not(self.contains(move[0], move[1]))): # TODO fix for jumping
                yield (piece, move)
    
    # Creates an iterable list of moves for a black piece
    def iterBlackPiece(self, piece):
        # White pieces can only move up the board
        possibleMove1 = (piece[0]+1, piece[1]+1)
        possibleMove2 = (piece[0]-1, piece[1]+1)
        print "possible moves for", piece, ":", possibleMove1, possibleMove2
        for move in (possibleMove1, possibleMove2):
            if ((move[0] > -1 and move[0] < self.width)
            and (move[1] > -1 and move[1] < self.height)
            and not(self.contains(move[0], move[1]))): # TODO fix for jumping
                print "from piece", piece, "we are going to try", move
                yield (piece, move)
            else:
                print move, "was eliminated"
    
    # Updates the array containing the board to reflect the current state
    # of the pieces on the board
    def updateBoard(self):
        for i in range(self.width):
            for j in range(self.height):
                self.boardState[i][j] = " "
        for piece in self.blacklist:
            self.boardState[piece[1]][piece[0]] = u'◆'
        for piece in self.whitelist:
            self.boardState[piece[1]][piece[0]] = u'◇'

    # Move a blackPiece from one spot to another
    def moveBlack(self, moveFrom, moveTo): 
        #TODO add better limits to bad move checking
        if (moveTo[0] > -1 and moveTo[0] < self.width):
            if (moveTo[1] > -1 and moveTo[1] < self.height):
                if not(self.contains(moveTo[0], moveTo[1])):
                    try:
                        self.blacklist[self.blacklist.index(moveFrom)] = moveTo
                    except ValueError:
                        print "The piece causing the error is", moveFrom
                        print "it was trying to move to", moveTo
                    self.printBoard()
                    self.turn = self.WHITE
                else:
                    print "Black Piece", moveFrom, "moving to", moveTo
                    raise Exception("MoveTo location already contains a piece!")
        
    def moveWhite(self, moveFrom, moveTo):
        #TODO add better limits to bad move checking
        if (moveTo[0] > -1 and moveTo[0] < self.width):
            if (moveTo[1] > -1 and moveTo[1] < self.height):
                print "The square we are moving to contains a piece", self.contains(moveTo[0], moveTo[1])
                print "White Piece", moveFrom, "moving to", moveTo
                if not(self.contains(moveTo[0], moveTo[1])):
                    #print "HERE"
                    self.whitelist[self.whitelist.index(moveFrom)] = moveTo
                    self.printBoard()
                    self.turn = self.BLACK
                else:
                    print "White Piece", moveFrom, "moving to", moveTo
                    raise Exception("MoveTo location already contains a piece!")
            else:
                print "I'M A DICK AND I TRIED TO MOVE OUT OF BOUNDS! FALALAH!"
        else:
            print "I'M A DICK AND I TRIED TO MOVE OUT OF BOUNDS! FALALAH!"
    
    def printBoard(self):
        print unicode(self)
        
    def __unicode__(self):
        lines = []
        # This prints the numbers at the top of the Game Board
        lines.append('    ' + '   '.join(map(str, range(self.width))))
        # Prints the top of the gameboard in unicode
        lines.append(u'  ╭' + (u'───┬' * (self.width-1)) + u'───╮')
        
        # Updates Game board
        self.updateBoard()
        
        # Print the boards rows
        for num, row in enumerate(self.boardState[:-1]):
            #lines.append(chr(num+65) + u' │ ' + u' │ '.join(row) + u' │')
            lines.append(str(num) + u' │ ' + u' │ '.join(row) + u' │')
            lines.append(u'  ├' + (u'───┼' * (self.width-1)) + u'───┤')
        
        #Print the last row
        #lines.append(chr(self.height+64) + u' │ ' + u' │ '.join(self.boardState[-1]) + u' │')
        lines.append(str(self.height-1) + u' │ ' + u' │ '.join(self.boardState[-1]) + u' │')

        # Prints the final line in the board
        lines.append(u'  ╰' + (u'───┴' * (self.width-1)) + u'───╯')
        return '\n'.join(lines)

    # Move without printing
    def moveSilentBlack(self, piece, move): 
        #TODO add better limits to bad move checking
        if ((move[0] > -1 and move[0] < self.width)
            and (move[1] > -1 and move[1] < self.height)
            and not(self.contains(move[0], move[1]))):
                try:
                    self.blacklist[self.blacklist.index(piece)] = move
                except ValueError:
                    print "The piece causing the error is", piece
                    print "it was trying to move to", move
                self.updateBoard()
                self.turn = self.WHITE
        else:
            raise Exception("Not a valid move dickweed!")
        
    def moveSilentWhite(self, piece, move):
        #TODO add better limits to bad move checking
        if ((move[0] > -1 and move[0] < self.width)
            and (move[1] > -1 and move[1] < self.height)
            and not(self.contains(move[0], move[1]))):
                self.whitelist[self.whitelist.index(piece)] = move
                self.updateBoard()
                self.turn = self.BLACK
        else:
            raise Exception("Not a valid move dickweed!")




#    def print_blank(self):
#        print blankboard(self)
## FOR BLANK BOARD ONLY
#    def __blankboard__(self):
#        lines = []
#        # This prints the numbers at the top of the Game Board
#        lines.append('    ' + '   '.join(map(str, range(self.width))))
#        # Prints the top of the gameboard in unicode
#        lines.append(u'  ╭' + (u'───┬' * (self.width-1)) + u'───╮')

#        # Print the boards rows
#        for num in range(self.height-1):
#            lines.append(str(num) + u' │  ' + (u' │  ' * (self.width-1)) + u' │')
#            lines.append(u'  ├' + (u'───┼' * (self.width-1)) + u'───┤')
#        
#        #Print the last row
#        lines.append(str(self.height) + u' │  ' + (u' │  ' * (self.width-1)) + u' │')

#        # Prints the final line in the board
#        lines.append(u'  ╰' + (u'───┴' * (self.width-1)) + u'───╯')
#        return '\n'.join(lines)
