# Provides the minmax functionality as well as static evaluation
from copy import deepcopy

def is_won(board):
    """
        Returns true if the game has been won
    """
    return board.gameWon <> board.NOTDONE
        

def minMax2(board):
    """
        Main minmax function, takes a board as input and returns the best possible move in the form
        of a board and the value of that board.
    """
    bestBoard = None
    currentDepth = board.maxDepth + 1
    while not bestBoard and currentDepth > 0:
        currentDepth -= 1
        # Get the best move and it's value from maxMinBoard (minmax handler)
        (bestBoard, bestVal) = maxMove2(board, currentDepth)
        # If we got a NUll board raise an exception
    if not bestBoard:
        raise Exception("Could only return null boards")
    # Otherwise return the board and it's value
    else:
        return (bestBoard, bestVal)

def maxMove2(maxBoard, currentDepth):
    """
        Calculates the best move for BLACK player (computer) (seeks a board with INF value)
    """
    return maxMinBoard(maxBoard, currentDepth-1, float('-inf'))
    

def minMove2(minBoard, currentDepth):
    """
        Calculates the best move from the perspective of WHITE player (seeks board with -INF value)
    """
    return maxMinBoard(minBoard, currentDepth-1, float('inf'))

def maxMinBoard(board, currentDepth, bestMove):
    """
        Does the actual work of calculating the best move
    """
    # Check if we are at an end node
    if is_won(board) or currentDepth <= 0:
        return (board, staticEval2(board))
  
    # So we are not at an end node, now we need to do minmax
    # Set up values for minmax
    best_move = bestMove
    best_board = None    
  
    # I could probably consolidate MaxNode and MinNode more by assigning the iterator with a 
    # function and doing some trickery with the bestmove == INF bullshit
    # MaxNode
    if bestMove == float('-inf'):
        # Create the iterator for the Moves
        moves = board.iterBlackMoves()
        for move in moves:
            maxBoard = deepcopy(board)
            maxBoard.moveSilentBlack(*move)
            value = minMove2(maxBoard, currentDepth-1)[1]
            if value > best_move:
                best_move = value
                best_board = maxBoard         
  
    # MinNode
    elif bestMove == float('inf'):
        moves = board.iterWhiteMoves()
        for move in moves:
            minBoard = deepcopy(board)
            minBoard.moveSilentWhite(*move)
            value = maxMove2(minBoard, currentDepth-1)[1]
            # Take the smallest value we can
            if value < best_move:
                best_move = value
                best_board = minBoard
  
    # Something is wrong with bestMove so raise an Exception
    else:
        raise Exception("bestMove is set to something other than inf or -inf")
  
    # Things appear to be fine, we should have a board with a good value to move to
    return (best_board, best_move)

def staticEval2(evalBoard):
    """
        Evaluates a board for how advantageous it is
        -INF if WHITE player has won
        INF if BLACK player has won
        Otherwise use a particular strategy to evaluate the move
        See Comments above an evaluator for what it's strategy is
    """
    # Has someone won the game? If so return an INFINITE value
    if evalBoard.gameWon == evalBoard.BLACK:
        return float('inf')  
    elif evalBoard.gameWon == evalBoard.WHITE:
        return float('-inf')
    # Unhappy Grandfather Evaluator
#    return 0
    
    # Some setup
    score = 0
    pieces = None   
    if evalBoard.turn == evalBoard.WHITE:
        pieces = evalBoard.whitelist
        scoremod = -1
    elif evalBoard.turn == evalBoard.BLACK:
        pieces = evalBoard.blacklist
        scoremod = 1

    # Super Gigadeath Defense Evaluator
    # This AI will attempt to keep it's peices as close together as possible until it has a chance
    # to jump the opposing player. It's super effective
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
    
    # Crouching Edge Hidden Victory Evaluator
    # not complete yet
    
    return score
