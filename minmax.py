# Provides the minmax functionality as well as static evaluation

def minMax(board, maxDepth):
    currentDepth = 0
    return maxMove(board, currentDepth, maxDepth)
    
def maxMove(board, currentDepth, maxDepth):
    if (board.isWon() or currentDepth >= maxDepth):
        return staticEval(board)
    else:
        bestMove = []
        moves = []
        generateMoves(moves) # x = iterWhiteMoves()
        for move in moves: # moves.next()
            move = minMove(testMove(board))
            if (staticEval(move) > staticEval(bestMove)
                bestMove = move
        return bestMove
        
def minMove(board, currentDepth, maxDepth):
    if (board.isWon() or currentDepth >= maxDepth):
        return
    
def staticEval(board):
    pass

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
