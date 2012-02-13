from copy import deepcopy

class Minimax(object):
    """
        Base class for minimax games. Subclasses should override is_ended, is_max,
        itermoves, and evaluate
    """
    def __init__(self, board):
        self.board = board
        
#    def justify(self, reason):
#        """Adds a reason for why this move was selected"""
#        if not hasattr(self, 'justification'):
#            self.justification = [reason]
#        else:
#            self.justification.append(reason)

    def is_ended(self):
        """
            Returns true if the game is over, false otherwise. Should be overridden
            in subclasses.
        """
        return self.board.gameWon >= 0

    def is_max(self):
        """
            Returns true if this node is a max node. Should be overridden in
            subclasses.
        """
        #TODO sketchy
        return self.board.turn == self.board.BLACK

    def itermoves(self):
        """
            Returns an iterable of all possible moves starting at the current state.
            Should be overridden in subclasses.
        """
        if self.board.turn == self.board.BLACK:
            for move in self.board.iterBlackMoves():
                temp = deepcopy(self.board)
                temp.moveSilentBlack(*move)
                yield Minimax(temp)
        else:
            for move in self.board.iterWhiteMoves():
                temp = deepcopy(self.board)
                temp.moveSilentWhite(*move)
                yield Minimax(temp)

    def evaluate(self):
        """
            Calculate the value of a game state and return it. Should be overridden
            by subclasses.
        """
        if self.board.gameWon == self.board.BLACK:
            return float('inf')
        elif self.board.gameWon == self.board.WHITE:
            return float('-inf')
        #return 0
        score = 0
        pieces = None
        if self.board.turn == self.board.WHITE:
            pieces = self.board.whitelist
            scoremod = -1
        elif self.board.turn == self.board.BLACK:
            pieces = self.board.blacklist
            scoremod = 1
        
        # Bundle AI, tries to keep it's pieces as close together as possible        
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

    def minimax(self, depth=0, minimum=float('-inf'), maximum=float('inf')):
        """
            Calculates the best possible move based on evaluate.  Returns a tuple
            (state, value, depth).
        """
        depth += 1
        if self.is_ended() or depth > self.board.max_depth:
            return (self, self.evaluate(), depth)
        shortest = float('inf')
        longest = 0
        draw_move = None
        win_move = None

        if self.is_max():
            value = float('-inf')
            for child in self.itermoves():
                (c, next, ndepth) = child.minimax(depth, value, maximum)
                if ndepth > longest:
                    draw_move = child
                    longest = ndepth
                if next > value or (next <> float('-inf') and next == value and ndepth < shortest):
                    value = next
                    win_move = child
                    shortest = ndepth
                    if value > maximum:
                        break
            if not win_move and draw_move:
                win_move = draw_move
                shortest = longest
            return (win_move, value, shortest)
        else:
            value = float('inf')
            for child in self.itermoves():
                (c, next, ndepth) = child.minimax(depth, minimum, value)
                if ndepth > longest:
                    draw_move = child
                    longest = ndepth
                if next < value or (next <> float('inf') and next == value and ndepth < shortest):
                    value = next
                    win_move = child
                    shortest = ndepth
                    if value < minimum:
                        break
            if not win_move and draw_move:
                win_move = draw_move
                shortest = longest
            return (win_move, value, shortest)
