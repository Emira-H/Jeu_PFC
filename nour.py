from random import randrangefrom math import ceildef choice_money():
   money=int(input("veuillez entrer le montant de la mise"))
   while money <= 0:
       print("erreur montant invalide, Veuillez resaisir votre montant de nouveau")
       money = int(input("veuillez entrer le montant de la mise"))
   print("vous avez choisi de miser {} euros".format(money))def choice_number():
   choice_player=int(input("veuillez choisir un nombre entre 0 et 49"))
   list_choice=list(range(50))
   while choice_player not in list_choice:
       print("erreur choix non valide, veuillez resaisir votre choix")
       choice_player =int(input("veuillez choisir un nombre entre 0 et 49"))
   print("vous avez choisi de miser sur {} ".format(choice_player))
   return choice_playerdef color(number):
   if int(number)%2==0:
       return "noir"
   else:
       return "rouge"def choice_random():
   choice_pc=randrange(50)
   print("le choix du pc est {}".format(choice_pc))
   return choice_pcdef game():
   first_money = choice_money()
   his_choice=choice_number()
   my_choice=choice_random()
   if his_choice==my_choice:
       first_money=3*first_money
   elif color(his_choice)==color(my_choice):
       first_money=ceil(first_money/2)
   else:
       first_money=0
   return first_moneyprint(list(range(50)))
choice_money()
game()


from random import randrangefrom math import ceildef choice_money():
   money=int(input("veuillez entrer le montant de la mise"))
   while money <= 0:
       print("erreur montant invalide, Veuillez resaisir votre montant de nouveau")
       money = int(input("veuillez entrer le montant de la mise"))
   print("vous avez choisi de miser {} euros".format(money))def choice_number():
   choice_player=int(input("veuillez choisir un nombre entre 0 et 49"))
   list_choice=list(range(50))
   while choice_player not in list_choice:
       print("erreur choix non valide, veuillez resaisir votre choix")
       choice_player =int(input("veuillez choisir un nombre entre 0 et 49"))
   print("vous avez choisi de miser sur {} ".format(choice_player))
   return choice_playerdef color(number):
   if int(number)%2==0:
       return "noir"
   else:
       return "rouge"def choice_random():
   choice_pc=randrange(50)
   print("le choix du pc est {}".format(choice_pc))
   return choice_pcdef game():
   first_money = choice_money()
   his_choice=choice_number()
   my_choice=choice_random()
   if his_choice==my_choice:
       first_money=3*first_money
   elif color(his_choice)==color(my_choice):
       first_money=ceil(first_money/2)
   else:
       first_money=0
   return first_moneyprint(list(range(50)))
choice_money()
game()
