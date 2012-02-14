# coding: utf-8
# Game board. It needs a height and a width in order
# to be instantiated
class board(object):
    BLACK = 1
    WHITE = 0
    NOTDONE = -1
    def __init__(self, height, width, firstPlayer):
        """
            Constructs a board, right now maxDepth is statically assigned
        """
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
        self.gameWon = self.NOTDONE
        self.turn = firstPlayer
        self.maxDepth = 10
    
    # Generate an iterator for all of the moves
    def iterWhiteMoves(self):
        """
            Main generator for white moves
        """
        for piece in self.whitelist:
            for move in self.iterWhitePiece(piece):
                yield move
                
    def iterBlackMoves(self):
        """
            Main Generator for black moves
        """
        for piece in self.blacklist:
            for move in self.iterBlackPiece(piece):
                yield move
                
    def iterWhitePiece(self, piece):
        """
            Generates possible moves for a white piece
        """            
        return self.iterBoth(piece, ((-1,-1),(1,-1)))
    
    def iterBlackPiece(self, piece):
        """
            Generates possible moves for a black piece
        """
        return self.iterBoth(piece, ((-1,1),(1,1)))

    def iterBoth(self, piece, moves):
        """
            Handles the actual generation of moves for either black or white pieces
        """
        for move in moves:
            # Regular Move
            targetx = piece[0] + move[0]
            targety = piece[1] + move[1]
            # If the move is out of bounds don't move
            if targetx < 0 or targetx >= self.width or targety < 0 or targety >= self.height:
                continue
            target = (targetx, targety)
            # Check that there is nothing in the way of moving to the target
            black = target in self.blacklist
            white = target in self.whitelist
            if not black and not white:
                yield (piece, target, self.NOTDONE)
            # There was something in the way, can we jump it?
            else:
                # It has to be of the opposing color to jump
                if self.turn == self.BLACK and black:
                    continue
                elif self.turn == self.WHITE and white:
                    continue
                # Jump proceeds by adding the same movement in order to jump over the opposing 
                # piece on the checkerboard
                jumpx = target[0] + move[0]
                jumpy = target[1] + move[1]
                # If the jump is going to be out of bounds don't do it.
                if jumpx < 0 or jumpx >= self.width or jumpy < 0 or jumpy >= self.height:
                    continue
                jump = (jumpx, jumpy)
                # Check that there is nothing in the jumpzone
                black = jump in self.blacklist
                white = jump in self.whitelist
                if not black and not white:
                    yield (piece, jump, self.turn)                   
    
    def updateBoard(self):
        """
            Updates the array containing the board to reflect the current state of the pieces on the
            board
        """
        for i in range(self.width):
            for j in range(self.height):
                self.boardState[i][j] = " "
        for piece in self.blacklist:
            self.boardState[piece[1]][piece[0]] = u'◆'
        for piece in self.whitelist:
            self.boardState[piece[1]][piece[0]] = u'◇'

    # Movement of pieces
    def moveSilentBlack(self, moveFrom, moveTo, winLoss): 
        """
            Move black piece without printing
        """
        if moveTo[0] < 0 or moveTo[0] >= self.width or moveTo[1] < 0 or moveTo[1] >= self.height:
            raise Exception("That would move black piece", moveFrom, "out of bounds")
        black = moveTo in self.blacklist
        white = moveTo in self.whitelist
        if not (black or white):
            self.blacklist[self.blacklist.index(moveFrom)] = moveTo
            self.updateBoard()
            self.turn = self.WHITE
            self.gameWon = winLoss
        else:
            raise Exception
        
    def moveSilentWhite(self, moveFrom, moveTo, winLoss):
        """
            Move white piece without printing
        """
        if moveTo[0] < 0 or moveTo[0] >= self.width or moveTo[1] < 0 or moveTo[1] >= self.height:
            raise Exception("That would move white piece", moveFrom, "out of bounds")
        black = moveTo in self.blacklist
        white = moveTo in self.whitelist
        if not (black or white):
            self.whitelist[self.whitelist.index(moveFrom)] = moveTo
            self.updateBoard()
            self.turn = self.BLACK
            self.gameWon = winLoss
        else:
            raise Exception
    
    def moveBlack(self, moveFrom, moveTo, winLoss):
        """
            Move a black piece from one spot to another. \n winLoss is passed as either 0(white)
            or 1(black) if the move is a jump
        """
        self.moveSilentBlack(moveFrom, MoveTo, winLoss)
        self.printBoard()
        
    def moveWhite(self, moveFrom, moveTo, winLoss):
        """
            Move a white piece from one spot to another. \n winLoss is passed as either 0(white)
            or 1(black) if the move is a jump
        """
        self.moveSilentWhite(moveFrom, moveTo, winLoss)
        self.printBoard()

    def printBoard(self):
        """
            Prints the game board to stdout
        """
        print unicode(self)
        
    def __unicode__(self):
        """
            Contains the unicode and other BS for printing the board
        """
        # Updates Game board
        self.updateBoard()
        lines = []
        # This prints the numbers at the top of the Game Board
        lines.append('    ' + '   '.join(map(str, range(self.width))))
        # Prints the top of the gameboard in unicode
        lines.append(u'  ╭' + (u'───┬' * (self.width-1)) + u'───╮')
        
        # Print the boards rows
        for num, row in enumerate(self.boardState[:-1]):
            lines.append(chr(num+65) + u' │ ' + u' │ '.join(row) + u' │')
            lines.append(u'  ├' + (u'───┼' * (self.width-1)) + u'───┤')
        
        #Print the last row
        lines.append(chr(self.height+64) + u' │ ' + u' │ '.join(self.boardState[-1]) + u' │')

        # Prints the final line in the board
        lines.append(u'  ╰' + (u'───┴' * (self.width-1)) + u'───╯')
        return '\n'.join(lines)

############## DEBUGGING
##############
#    def getWin(self):
#        return self.g
#    
#    def setWin(self, val):
##        if val == 0:
##            raise Exception("Game won by white")
#        self.g = val

#    gameWon=property(getWin, setWin)
##############
##############
