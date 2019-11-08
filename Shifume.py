'''Etape Insertion Nom:création de la fonction add_Name(name_user)'''
import random


def add_Name():

    name_player = input("Merci de renseigner votre nom: ")

    while len(name_player) == 0:

        msg_noname = "Vous n'avez rien renseigné"
        print(msg_noname)

        name_player = input("Merci de renseigner votre nom: ")
#message to welcome the player
    msg_welcome = "Bienvenue {} sur le jeu SHIFUMI!".format(name_player)

    print(msg_welcome)
#message to explain how to do the choice

    msg_rule = "Pour jouer, il vous suffit de taper la première lettre de votre choix. Pour choisir pierre, feuille ou ciseaux, veuillez taper respectivement sur la touche P, F ou C"

    print(msg_rule)

    return name_player

name=add_Name()

Score=0
Score_PC=0
#Choice of value
while Score<3:
    def Value_player():
        choice = input("Entrer P, F ou C! A vous de jouer! ").upper()

        while choice not in ["P","F","C"]:
            print("choix invalide")
            choice = input("Entrer P, F ou C! A vous de jouer! ").upper()

        if choice == 'P':
            print("Vous avez choisi PIERRE")

        elif choice == 'F':
            print("vous avez choisi FEUILLE")

        elif choice == 'C':
            print("vous avez choisi CISEAUX")

        return choice

    Value_player()

    #create function PC_value
    lib ={'P':'PIERRE', 'F':'FEUILLE', 'C':'CISEAUX'}

    def PC_value():
        choice_PC = random.choice(['P','F','C'])

        print("L'ordinateur a joué {}".format(lib[choice_PC]))
        return choice_PC
    PC_value()

    # Comparaison des valeurs
    # creation of a tuple with choice of the player and the choice of the computer

    play_now = (choice,choice_PC)
    print(play_now)

    #create a list with the win choices for the name_player


    win_player = [('P','C'), ('F','P'), ('C','F')]
    def player_Win():
        for i,j in enumerate(win_player):
            if play_now == win_player[i]:
                return True


    if player_Win() == True:
        Score = Score + 1
    elif player_Win()== False and choice_PC == choice:
        Score_PC = Score_PC + 1

print(player_Win())
print(Score)
print(Score_PC)
