from functions import insert_name, choices, player_win

name_player = insert_name()

score_player = 0
score_pc = 0

choice_game = choices()


while score_player < 3 and score_pc < 3:

    if player_win():
        score_player = score_player + 1
        print("Votre score est de {} contre {} pour votre adversaire, rejouez!\n".format(score_player,score_pc))
    elif not player_win() and choice_game[0] != choice_game[1]:
        score_pc = score_pc + 1
        print("Votre score est de {} contre {} pour votre adversaire, rejouez!\n".format(score_player,score_pc))
    if choice_game[0] == choice_game[1]:
        print("Le match est nul. Rejouez! \n")
