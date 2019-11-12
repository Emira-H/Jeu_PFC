# import functions of file functions
from functions import choice_player, choice_pc, player_wins, game

#input to insert name of the player with control input (error message if name is none)
name_player = input("Merci de renseigner votre nom: ").upper()
while len(name_player) == 0:
    print("Vous n'avez rien renseigné")
    name_player = input("Merci de renseigner votre nom\n: ").upper()
#print message to welcome and to explain the choices values
print("********Bienvenue {} sur le jeu SHIFUMI!*********\n".format(name_player))
print("Pour choisir PIERRE, FEUILLE ou CISEAUX, veuillez taper la première lettre de votre choix (P, F ou C)\n")


#loop for replaying each time after a input
replay_game = True
while replay_game:
    game()
    Replay=input("Taper R pour rejouer une partie ou 'Q' pour quitter ").lower()
    if Replay =='q':
        replay_game = False
        print("Merci et à bientôt sur SHIFUMI!")
