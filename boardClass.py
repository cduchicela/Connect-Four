
class Board:
    ''' Creates a board for a Connect Four game
    '''

    def __init__(self, height, width):
        ''' Creates a new Board with the height, width, and
        the slots in every row/column of the board
        '''
        self.height = height
        self.width = width
        self.slots = [['  '] * width for row in range(self.height)]

    def __repr__(self):
        """ Redefines str to return a string representation for a Board.
        """
        s = ''         
        for row in range(self.height):
            s += '|'   
            for col in range(self.width):
                s += self.slots[row][col] + '|'
            s += '\n'  
        s += (2*self.width + 1) *  '- '
        s += '\n'
        s += ' '
        for col in range(self.width):
            if col > 9:
                col = col % 10
            s += str(col)
            s += ' '
        return s


    def add_checker(self, checker, col):
        ''' adds the specified checker to  col
        of the called Board
        '''
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)
        row = 0
        while self.slots[row][col] == '  ': 
            row += 1
            if row == self.height - 1:
                break
        if self.slots[row][col] != '  ':
            row += -1
            
        self.slots[row][col] = checker

    def reset(self):
        ''' Clears the Board on which it is called by setting all slots
        to contain a " "
        '''
        for row in range(self.height):
            for col in range(self.width):
                self.slots[row][col] = '  '

    def add_checkers(self,colnums):

        checker = 'X'
        for col_str in colnums:
            col=int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker,col)
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    def can_add_to(self,col):
        ''' returns True if it is valid to place a checker in the column
        on the Board. Otherwise, returns False
        '''

        if col < 0:
            return False
        elif col > self.width-1:
            return False
        elif self.slots[0][col] != '  ':
            return False
        else:
            return True

    def is_full(self):
        ''' returns True if the Board is full and
        returns False otherwise
        '''
        for col in range(self.width):
            if self.can_add_to(col):
                return False
        
        return True

    def remove_checker(self, col):
        ''' removes the top checker from column col of the called Board object.
        if the column is empty, then does nothing.
        '''
        for row in range(self.height):
            if self.slots[row][col] != ' ':
                self.slots[row][col] = ' '
                return

    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):

                
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True
        return False
            
    def is_vertical_win(self, checker):
        ''' Checks for a vertical win for the specified checker.
        '''
        for row in range(self.height-3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                   self.slots[row+1][col] == checker and \
                   self.slots[row+2][col] == checker and \
                   self.slots[row+3][col] == checker:
                    return True
        return False
    
    def is_up_diagonal_win(self, checker):
        ''' Checks for a diagonal-up win for the specified checker
        '''
        for row in range(3,self.height):
            for col in range(self.width-3):
                if self.slots[row][col] == checker and \
                   self.slots[row-1][col+1] == checker and \
                   self.slots[row-2][col+2] == checker and \
                   self.slots[row-3][col+3] == checker:
                    return True
        return False

    def is_down_diagonal_win(self, checker):
        ''' Checks for a diagonal-down win for the specified checker
        '''
        for row in range(self.height-3):
            for col in range(self.width-3):
                if self.slots[row][col] == checker and \
                   self.slots[row+1][col+1] == checker and \
                   self.slots[row+2][col+2] == checker and \
                   self.slots[row+3][col+3] == checker:
                    return True
        return False
                
    def is_win_for(self, checker):
        ''' accepts a parameter checker that is either 'X' or 'O', and returns
        True if there are four consecutive slots containing checker on the board.
        Otherwise, returns False
        '''
        assert(checker == 'X' or checker == 'O')
        if self.is_down_diagonal_win(checker) == True:
            return True
        if self.is_up_diagonal_win(checker) == True:
            return True
        if self.is_vertical_win(checker) == True:
            return True
        if self.is_horizontal_win(checker) == True:
            return True
        return False
    



