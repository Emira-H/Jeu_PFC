import random


def player_wins():
    choices = ('P', 'C')
    win_tuples = [('C','F'),('P','C'), ('F','P')]
    #for i,j in enumerate(win_tuples):
    if choices in win_tuples:
        return True
    else:
        return False
print(player_wins())
