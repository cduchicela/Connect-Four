import random
from ps14pr3 import * # to use the connect_four and process_move functions


class RandomPlayer(Player): #ask why col is undefined 
    def next_move(self, board):
        column=[]
        for i in range(board.width):
            if can_add_to():
                column+=[i]
        return random.choice(col)


#def next move(self board)
 #       column=[]
 #        for i in range(board.width):
 #            if can_add_to(col):
 #                col[i]
 #                column+=1
 #                return random.choice(col)


# Hi, im not with my laptop right now but think my code for random - next move was:

 
