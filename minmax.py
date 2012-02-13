# Provides the minmax functionality as well as static evaluation
from copy import deepcopy

def minMax(board, maxDepth):
    currentDepth = 0
    (tempBoard, miscVal) = minMove(board, currentDepth, maxDepth)
    if not tempBoard:
#        print "The returned board was Null, lowering depth by 1"
        (tempBoard, miscVal) = minMax(board, maxDepth-1)
    #tempBoard.printBoard()
    return (tempBoard, miscVal)
    
def maxMove(board, currentDepth, maxDepth):
#    print '===MAX MOVE==='
    if (board.gameWon <> -1) or (currentDepth >= maxDepth):
#        print 'LEAF NODE', board.gameWon
        test = staticEval(board)
        if not board:
            raise Exception("MaxMove is a dick")
        return (board, test)
    else:
#        print 'NODE'
        bestMove = float("-inf")
        bestBoard = None
        # Depending on the turn, we create an iterator for the appropriate player
        #print board.turn
        if board.turn == 1: # Black
            movesB = board.iterBlackMoves()
            for move in movesB:
                # We have to use a copy of the board so that when we recurse back
                # we do not end up using a modified board for the next move
                outBoard = deepcopy(board)
                outBoard.updateBoard()
                #board.moveBlack(*move)
                outBoard.moveSilentBlack(*move)
                (bangarangMotherfucker, value) = minMove(outBoard, currentDepth+1, maxDepth)
                if value > bestMove:
                    print (bangarangMotherfucker, value)
                    bestMove = value
                    bestBoard = outBoard
                    
            if not bestBoard:
                print "****FUCKUP BOARD****"
                board.printBoard()
                raise Exception("MaxMove tried to move black, at depth", currentDepth, "bestValue was", bestMove)
            return (bestBoard, bestMove)
            
        else: # White
            movesW = board.iterWhiteMoves()
            for move in movesW:
                outBoard = deepcopy(board)
                outBoard.updateBoard()
                #board.moveWhite(*move)
                outBoard.moveSilentWhite(*move)
                (bangarangMotherfucker, value) = minMove(outBoard, currentDepth+1, maxDepth)
                if value > bestMove:
                    bestMove = value
                    bestBoard = outBoard
            if not bestBoard:
                raise Exception("MaxMove tried to move white, at depth", currentDepth)
            return (bestBoard, bestMove)
        
def minMove(board, currentDepth, maxDepth):
#    print '***MINMOVE***'
#    board.printBoard()
    if (board.gameWon <> -1) or (currentDepth >= maxDepth):
        if not board:
            raise Exception("MinMove is a dick")
        return (board, staticEval(board))
    else:
        bestMove = float("inf")
        bestBoard = None 
        # Depending on the turn, we create an iterator for the appropriate player
        if board.turn == 1: # Black
            moves = board.iterBlackMoves()
            for move in moves:
                outBoard = deepcopy(board)
                outBoard.updateBoard()
                #board.moveBlack(*move)
                outBoard.moveSilentBlack(*move)
                (bangarangMotherfucker, value) = maxMove(outBoard, currentDepth+1, maxDepth)
                outBoard.updateBoard()
                if value < bestMove:
                    bestMove = value
                    bestBoard = outBoard
            if not bestBoard:
                raise Exception("MinMove tried to move black, at depth", currentDepth)
            return (bestBoard, bestMove)
        else: # White
            moves = board.iterWhiteMoves()
            for move in moves:
                outBoard = deepcopy(board)
                outBoard.updateBoard()
                #board.moveWhite(*move)
                outBoard.moveSilentWhite(*move)
                (bangarangMotherfucker, value) = maxMove(outBoard, currentDepth+1, maxDepth)
                outBoard.updateBoard()
                if value < bestMove:
                    print (bangarangMotherfucker, value)
                    bestMove = value
                    bestBoard = outBoard
            if not bestBoard:
                raise Exception("MinMove tried to move white, at depth", currentDepth)
            return (bestBoard, bestMove)
    
def staticEval(board):
    if board.gameWon == board.BLACK:
        return float('inf')
    elif board.gameWon == board.WHITE:
        return float('-inf')
        
    board.updateBoard()
    score = 0
    scoremod = 1
    if board.turn == board.WHITE:
        pieces = board.whitelist
        scoremod = -1
    else:
        pieces = board.blacklist
    
    # Bundle AI, tries to keep it's peices as close together as possible        
    distance = 0
    for piece1 in pieces:
        for piece2 in pieces:
            if piece1 == piece2:
                continue
            dx = abs(piece1[0] - piece2[0])
            dy = abs(piece1[1] - piece2[1])
            distance += dx**2 + dy**2
    distance /= len(pieces)
    score = 1.0/distance * scoremod
    
    # Wall AI, tries to keep pieces near the walls
    
    return score
