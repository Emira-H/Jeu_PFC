'''Etape Insertion Nom:création de la fonction add_Name(name_user)'''


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


#Choice of value

def Value_player():
    choice = input("Entrer P, F ou C! A vous de jouer! ").upper()

    while choice not in ["P","F","C"]:
        print("choix invalide")
        choice = input("Entrer P, F ou C! A vous de jouer! ").upper()

    if choice == "P":
        print("Vous avez choisi PIERRE")

    elif choice == "F":
        print("vous avez choisi FEUILLE")

    elif choice == "C":
        print("vous avez choisi CISEAUX")

    return choice

choix = Value_player()
