#Algo tirer de CodeWars, Lance X dés 20 dans une tranche de valeur comprise en 2 et 11 c'est Moyen, 11 et 20 c'est reussit
#et si c'est egal à 1 c'est un Echec Critique et egal à 20 c'est une reussite critique 

import random

def dice_roll():
    roll = int(input("Number of dice roll : ")) 
    dice = []
    for i in range(roll):
        value = random.randint(1, 20)
        dice.append(value)
    print(dice)

    for x in dice:
        if x == 1:
            print("Critical Failure")
        if 2 <= x <= 11:
            print("Medium")
        if 11 <= x < 20:
            print("Success")
        if x == 20:
            print("Critical Success")
dice_roll()

#Algo qui prend en Input le nombre de des voulut ainsi que le nombre de fois qu'on le lance qui fait une liste puis les regroupe en une seule liste
#Enleve la valeur la plus petite et fait une somme total des dés 

def roll():
    nb_dice = int(input("Number of dice : "))
    sum_dice = []
    nb_roll = int(input("Number of dice roll : "))

    for i in range(nb_roll):
        dice = [random.randint(1, 6) for x in range(nb_dice)]
        print(dice)
        dice.remove(min(dice))
        stat = sum(dice)
        print(stat)
        sum_dice.append(dice)
    print(sum_dice)

roll()