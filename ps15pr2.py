#
# ps15pr2.py (Problem Set 15, Problem 2)
#
# An AI Player for use in Connect Four
#

import random
from ps14pr3 import * # to use the connect_four and process_move functions

class AIPlayer(Player):
    ''' An AIPlayer for the connect four game.
    Checker should be "X" or "O"
    tiebreak should be "LEFT" "RIGHT" or "RANDOM"
    lookahead should be an integer from 0-4
    
    '''
    def __init__(self, checker, tiebreak, lookahead):
        ''' Constructs a new AIPlayer object
        '''
        Player.__init__(self, checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead

    def __repr__(self): #repr
        ''' returns a string representing an AIPlayer
        '''
        return('Player ' + self.checker + ' (' + self.tiebreak + ', ' + str(self.lookahead) + ')')

    def max_score_column(self, scores):
        ''' takes a list scores containing a score for each column of the board
        and returns the index of the column with the maximum score. Applies
        tiebreaking strategy to break any ties
        '''
        max_scores = []
        for i in range(len(scores)):
            if scores[i] == max(scores):
                max_scores += [i]
        if self.tiebreak == 'LEFT':
            return max_scores[0]
        if self.tiebreak == 'RIGHT':
            return max_scores[-1]
        if self.tiebreak == 'RANDOM':
            return random.choice(max_scores)

    def scores_for(self, board):
        ''' takes a Board and determines the called AIPlayer's
        scores for the columns in board
        '''
        scores = [50] * len(range(board.width)) #50*board,width

        for col in range(board.width):
            if not board.can_add_to(col):
                scores[col] = -1
            elif board.is_win_for(self.checker):
                scores[col] = 100
            elif board.is_win_for(self.opponent_checker()):
                scores[col] = 0
            elif self.lookahead == 0 :
                scores[col] = 50
            else:
                board.add_checker(self.checker, col)
                other_player = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead-1)
                other_scores = other_player.scores_for(board)
                if max(other_scores) == 0:
                    scores[col] = 100
                elif max(other_scores) == 100:
                    scores[col] = 0
                elif max(other_scores) == 50:
                    scores[col] = 50
                    
                board.remove_checker(col)
        return scores

    def next_move(self, board):
        ''' returns the  AIPlayer's judgement of its best possible move
        '''
        self.num_moves += 1
        scores = self.scores_for(board)
        return self.max_score_column(scores)
