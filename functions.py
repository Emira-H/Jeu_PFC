import random

# function add_name: add name user from a input, return name_player, loop if no name insertion, messages to welcome and explain the rules to choice a value
def insert_name():
    name_player = input("Merci de renseigner votre nom: ").upper()
    while len(name_player) == 0:
        print("Vous n'avez rien renseigné")
        name_player = input("Merci de renseigner votre nom\n: ").upper()
    print("********Bienvenue {} sur le jeu SHIFUMI!*********\n".format(name_player))
    print("Pour choisir PIERRE, FEUILLE ou CISEAUX, veuillez taper la première lettre de votre choix soit P, F ou C")
    return name_player


# function to add the choices from the player with an input and loop to demand the good choice if mistake
# function to add the choice of computer with a random

def choices():
    label = {'P':'PIERRE', 'F':'FEUILLE', 'C':'CISEAUX'}

    choice_player = input("Entrer P, F ou C! A vous de jouer!\n ").upper()
    while choice_player not in label:
        print("Votre saisie n'est pas valide!")
        choice_player = input("A vous de jouer, tapez P, F ou C! ").upper()
    print("Vous avez choisi {}\n".format(label[choice_player]))
    choice_pc = random.choice(['P','F','C'])
    print("L'ordinateur a joué {} \n".format(label[choice_pc]))
    choice_game = (choice_player, choice_pc)
    return choice_game


# function comparing the tuple of value player and value PC and return True if the winner is the player
def player_win():
    choice_game = choices()
    win_player = [('P','C'), ('F','P'), ('C','F')]
    for i,j in enumerate(win_player):
        if choice_game == win_player[i]:
            return True
