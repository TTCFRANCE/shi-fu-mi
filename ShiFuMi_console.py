from random import *
import time

#Variables principales de jeu
tour = 0
victory_P1 = 0
victory_com = 0

print("Bienvenue dans le jeu ShiFuMi !")
print("Pour gagner la partie tu doit gagné 3 manches")
print("Tu auras 3 choix possible :")
print("1: Pierre, 2: Papier, 3: Ciseaux")

while tour<3:
    computer_choice = randint(1, 3)
    print("Tour :" , tour + 1)
    player_choice = int(input("Quel choix fait tu ? "))
    if player_choice == 1:
        P1_choice = "Pierre"
        pass
    elif player_choice == 2:
        P1_choice = "Papier"
        pass
    elif player_choice == 3:
        P1_choice = "Ciseaux"
        pass
    else:
        print("Ton choix n'est pas possible.")
        continue

    if 1<=player_choice<=3:
        print("Shi Fu Mi !")
        time.sleep(0.7)

    if computer_choice == 1:
        com_choice = "Pierre"
    elif computer_choice == 2:
        com_choice = "Papier"
    elif computer_choice == 3:
        com_choice = "Ciseaux"
    
    if com_choice == P1_choice:
        print("L'ordinateur à aussi jouer :" , com_choice)
        computer_choice = randint(1, 3)
        continue
    elif com_choice != P1_choice:
        if com_choice == "Ciseaux" and P1_choice == "Papier":
            print("L'ordinateur a fait", com_choice)
            print("Tu as perdu !")
            victory_com = victory_com + 1
            tour = tour + 1
        elif com_choice == "Ciseaux" and P1_choice == "Pierre":
            print("L'ordinateur a fait", com_choice)
            print("Tu as gagné !")
            victory_P1 = victory_P1 + 1
            tour = tour + 1
        elif com_choice == "Papier" and P1_choice == "Ciseaux":
            print("L'ordinateur a fait", com_choice)
            print("Tu as gagné !")
            victory_P1 = victory_P1 + 1
            tour = tour + 1
        elif com_choice == "Papier" and P1_choice == "Pierre":
            print("L'ordinateur a fait", com_choice)
            print("Tu as perdu !")
            victory_com = victory_com + 1
            tour = tour + 1
        elif com_choice == "Pierre" and P1_choice == "Papier":
            print("L'ordinateur a fait", com_choice)
            print("Tu as gagné !")
            victory_P1 = victory_P1 + 1
            tour = tour + 1
        elif com_choice == "Pierre" and P1_choice == "Ciseaux":
            print("L'ordinateur a fait", com_choice)
            print("Tu as perdu !")
            victory_com = victory_com + 1
            tour = tour + 1
if victory_com > victory_P1:
    print(" L'ordinateur t'as battu", victory_com, "à", victory_P1)
elif victory_P1 > victory_com:
    print(" Tu as battu l'ordinateur", victory_P1, "à", victory_com)