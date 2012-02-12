# Provides the minmax functionality as well as static evaluation
from copy import deepcopy

def minMax(board, maxDepth):
    currentDepth = 0
    return maxMove(board, currentDepth, maxDepth)
    
def maxMove(board, currentDepth, maxDepth):
    print "*********ENTERING MAXMOVE*********"
    print "maxMove depth is", currentDepth
    if board.turn == board.WHITE:
        print "!!It is WHITES turn!!"
    elif board.turn == board.BLACK:
        print "!!It is BLACKS turn!!"
    else:
        print "!!!!!!!!!!!WHAT THE FUCKING CHRIST IS GOING ON???!!!!!!!"
    board = deepcopy(board)
    if board.gameWon or (currentDepth >= maxDepth):
        if board.gameWon:
            print "game was won"
        elif currentDepth >= maxDepth:
            print "Current Depth exceeds max Depth. Returning original Board"
        return (board, staticEval(board))
    else:
        bestMove = float("-inf")
        bestBoard = None
        # Depending on the turn, we create an iterator for the appropriate player
        #print board.turn
        if board.turn == 1: # Black
            movesB = board.iterBlackMoves()
            #print "moves", moves
            for move in movesB:
                #board.moveSilentBlack(*move)
                print "*********BLACKS MAX MOVE*********"
                print "Move", move
                board.updateBoard()
                board.moveBlack(*move)
                (board, value) = minMove(board, currentDepth+1, maxDepth)
                if value > bestMove:
                    bestMove = value
                    bestBoard = board
            return (bestBoard, bestMove)
        else: # White
            movesW = board.iterWhiteMoves()
            for move in movesW:
                #board.moveSilentWhite(*move)
                print "*********WHITES MIN MOVE*********"
                print "Move", move
                board.moveWhite(*move)
                (board, value) = minMove(board, currentDepth+1, maxDepth)
                if value > bestMove:
                    bestMove = value
                    bestBoard = board
            return (bestBoard, bestMove)
        
def minMove(board, currentDepth, maxDepth):
    print "*********ENTERING MINMOVE*********"
    print "minMove depth is", currentDepth
    if board.turn == board.WHITE:
        print "!!It is WHITES turn!!"
    elif board.turn == board.BLACK:
        print "!!It is BLACKS turn!!"
    else:
        print "!!!!!!!!!!!WHAT THE FUCKING CHRIST IS GOING ON???!!!!!!!"
    board = deepcopy(board)
    if board.gameWon or (currentDepth >= maxDepth):
        if board.gameWon:
            print "game was won"
        elif currentDepth >= maxDepth:
            print "Current Depth exceeds max Depth. Returning original Board"
        return (board, staticEval(board))
    else:
        bestMove = float("inf")
        bestBoard = None 
        # Depending on the turn, we create an iterator for the appropriate player
        if board.turn == 1: # Black
            moves = board.iterBlackMoves()
            for move in moves:
                #board.moveSilentBlack(*move)
                print "*********BLACKS MIN MOVE*********"
                board.moveBlack(*move)
                (board, value) = maxMove(board, currentDepth+1, maxDepth)
                board.updateBoard()
                if value < bestMove:
                    bestMove = value
                    bestBoard = board
            return (bestBoard, bestMove)
        else: # White
            moves = board.iterWhiteMoves()
            for move in moves:
                #board.moveSilentWhite(*move)
                print "*********WHITES MIN MOVE*********"
                board.moveWhite(*move)
                (board, value) = maxMove(board, currentDepth+1, maxDepth)
                board.updateBoard()
                if value < bestMove:
                    bestMove = value
                    bestBoard = board
            return (bestBoard, bestMove)
    
def staticEval(board):
    return 0
