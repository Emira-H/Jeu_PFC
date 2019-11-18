import random

#choice of the player in a list
def choice_player():
    lib ={'P':'PIERRE', 'F':'FEUILLE', 'C':'CISEAUX'}
    choice_player = input("Entrer P, F ou C! A vous de jouer! \n").upper()
    print("Vous avez joué {}\n".format(lib[choice_player]))
    while choice_player not in ['P','F','C']:
        print("choix invalide")
        choice_player = input("Entrer P, F ou C! A vous de jouer! \n").upper()
    return choice_player

#choice of the computer with a function random
def choice_pc():
    lib ={'P':'PIERRE', 'F':'FEUILLE', 'C':'CISEAUX'}
    choice_pc = random.choice(['P','F','C'])
    print("L'ordinateur a joué {}\n".format(lib[choice_pc]))
    return choice_pc



#function which define if the player is winning
#search if the tuple(choice, choice_pc) is in the list of tuples wich contains the win's tuples and return a boolean (with a loop)
def player_wins(choices):
    choices = (choice_player, choice_pc)
    win_tuples = [('C','F'),('P','C'), ('F','P')]
    if choices in win_tuples:
        return True
    else:
        return False

# create the variables which stock the scores of player and PC
# add a point to each score and print the scores for each choice by comparing the both choices of the player and the PC
# loop while to replay each time until the score reaches 3 points and print the winner

def game():
    score = 0
    score_pc = 0
    while score < 3 and score_pc <3:
        choices= (choice_player(),choice_pc())
        print(choices)
        if player_wins(choices) is True:
            score = score + 1
            print("Votre score est de {} contre {} pour votre adversaire\n".format(score,score_pc))
        elif player_wins(choices) is False and choices[0] != choices[1]:
            score_pc = score_pc + 1
            print("Votre score est de {} contre {} pour votre adversaire\n".format(score,score_pc))
        else:
            print("Votre score est de {} contre {} pour votre adversaire\n".format(score,score_pc))
    if score_pc == 3:
        print("Dommage, vous avez perdu!")
    else:
        print("Bravo, Vous avez gagné!")
