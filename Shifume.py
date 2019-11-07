'''Etape Insertion Nom:création de la fonction add_Name(name_user)'''


def add_Name():

    name_player = input("Merci de renseigner votre nom: ")

    while len(name_player) == 0:
        msg_noname = "Vous n'avez rien renseigné"
        print(msg_noname)
        name_player = input("Merci de renseigner votre nom: ")

    print("Bienvenue {} sur le jeu SHIFUMI!".format(name_player))
    return name_player

name=add_Name()
