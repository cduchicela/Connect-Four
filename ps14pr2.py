from ps14pr1 import Board

class Player:
    ''' Represents a player of the connect four game. Input either "X" or "O"
    as a checker. 
    '''
    def __init__(self, checker):
        ''' constructs a new Player by creating num_moves and checker
        attributes
        '''

        if checker in "XO":
            self.checker = checker
            self.num_moves = 0
        else:
            print('Your checker must be either "X" or "O" (case sensitive).')
                

    def __str__(self):
        ''' redefines str to return a string of the Player that calls it
        '''
        return 'Player ' + str(self.checker)

    def __repr__(self):
        ''' returns a string representing the Player that calls it
        '''
        return str(self)
    
    def opponent_checker(self):
        ''' returns a one-character string representing the checker of the
        Player's opponent
        '''
        if self.checker == 'X':
            return 'O'
        if self.checker == 'O':
            return 'X'

    def next_move(self, board):
        ''' Takes a Board as a parameter and returns the column
        where the player wants to make the next move
        '''
        self.num_moves += 1
            
        while True:
            colstr = input('Enter a column: ')
            if colstr in "0123456":
                colnum = int(colstr)
                if board.can_add_to(colnum):
                    return colnum
            print('Try again!')

