# Provides the minmax functionality as well as static evaluation

def minMax(board, maxDepth):
    currentDepth = 0
    return maxMove(board, currentDepth, maxDepth)
    
def maxMove(board, currentDepth, maxDepth):
    if board.gameWon or currentDepth >= maxDepth:
        return staticEval(board)
    else:
        bestMove = ()
        moves = []
        
        # Depending on the turn, we create an iterator for the appropriate player
        if board.turn == 1: # White
            moves = board.iterBlackMoves()
        else: # Black
            moves = board.iterWhiteMoves()
        
        for move in moves.next():
            move = minMove(testMove(board))
            if staticEval(move) > staticEval(bestMove):
                bestMove = move
        return bestMove
        
def minMove(board, currentDepth, maxDepth):
    bestMove = ()
    moves = []
    
    # Depending on the turn, we create an iterator for the appropriate player
    if board.turn == 1: # White
        moves = board.iterBlackMoves() # generateMoves(moves)
    else:
        moves = board.iterWhiteMoves()
    
    for move in moves.next():
        move = maxMove(board.move)
        if staticEval(move) > staticEval(bestMove):
            bestMove = move
    return bestMove
    
def staticEval(board):
    return 0

#    MinMax (GamePosition game) {
#      return MaxMove (game);
#    }
#     
#    MinMove (GamePosition game) {
#      best_move <- {};
#      moves <- GenerateMoves(game);
#      ForEach moves {
#         move <- MaxMove(ApplyMove(game));
#         if (Value(move) > Value(best_move)) {
#            best_move < - move;
#         }
#      }
#     
#      return best_move;
#    }
#   
#    MaxMove (GamePosition game) {
#      if (GameEnded(game)) {
#        return EvalGameState(game);
#      }
#      else {
#        best_move < - {};
#        moves <- GenerateMoves(game);
#        ForEach moves {
#           move <- MinMove(ApplyMove(game));
#           if (Value(move) > Value(best_move)) {
#              best_move < - move;
#           }
#        }
#        return best_move;
#      }
#    }
