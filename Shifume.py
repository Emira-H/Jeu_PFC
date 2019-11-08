'''Etape Insertion Nom:création de la fonction add_Name(name_user)'''
import random

# function add_name: add name user from a input, return name_player, loop if no name insertion, messages to welcome and explain the rules to choice a value
def add_Name():

    name_player = input("Merci de renseigner votre nom: ")

    while len(name_player) == 0:

        msg_noname = "Vous n'avez rien renseigné"
        print(msg_noname)

        name_player = input("Merci de renseigner votre nom: ")

    msg_welcome = "Bienvenue {} sur le jeu SHIFUMI!".format(name_player)

    print(msg_welcome)

    msg_rule = "Pour jouer, il vous suffit de taper la première lettre de votre choix. Pour choisir pierre, feuille ou ciseaux, veuillez taper respectivement sur la touche P, F ou C"

    print(msg_rule)

    return name_player


# function to add the values chosen by the player from an input and loop to demand the good values if mistake
def Value_player():

    choice = input("Entrer P, F ou C! A vous de jouer! ").upper()

    while choice not in ['P','F','C']:
        print("choix invalide")
        choice = input("Entrer P, F ou C! A vous de jouer! ").upper()

    if choice == 'P':
        print("Vous avez choisi PIERRE")

    elif choice == 'F':
        print("vous avez choisi FEUILLE")

    elif choice == 'C':
        print("vous avez choisi CISEAUX")

    return choice

# function to add the values of computer with a random
def PC_value():

    lib ={'P':'PIERRE', 'F':'FEUILLE', 'C':'CISEAUX'}

    choice_PC = random.choice(['P','F','C'])

    print("L'ordinateur a joué {}".format(lib[choice_PC]))
    return choice_PC


# function comparing the tuple of value player and value PC and return True if the winner is the player
def player_Win():
    win_player = [('P','C'), ('F','P'), ('C','F')]
    for i,j in enumerate(win_player):
        if play_now == win_player[i]:
            return True
        else:
            return False


add_Name()


Score=0
Score_PC=0

while Score<3 and Score_PC<3:

    play_now = (Value_player(),  PC_value())

    player_Win()

    if player_Win() == True:
        Score = Score + 1
        print("Votre score est de {} contre {} pour votre adversaire".format(Score,Score_PC))

    elif player_Win() == False and play_now[0] != play_now[1]:
        Score_PC = Score_PC + 1
        print("Votre score est de {} contre {} pour votre adversaire".format(Score,Score_PC))
