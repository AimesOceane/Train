#Algo tirer de CodeWars, Lance X dés 20 dans une tranche de valeur comprise en 2 et 11 c'est Moyen, 11 et 20 c'est reussit
#et si c'est egal à 1 c'est un Echec Critique et egal à 20 c'est une reussite critique 

import random

def lancer_des():
    lancer = int(input("Nombre de des lancer : ")) 
    des = []
    for i in range(lancer):
        de = random.randint(1, 20)
        des.append(de)
    print(des)

    for x in des:
        if x == 1:
            print("Echec Critique")
        if 2 <= x <= 11:
            print("Moyen")
        if 11 <= x < 20:
            print("Reussite")
        if x == 20:
            print("Reussite Critique")
lancer_des()

#Algo qui prend en Input le nombre de des voulut ainsi que le nombre de fois qu'on le lance qui fait une liste puis les regroupe en une seule liste
#Enleve la valeur la plus petite et fait une somme total des dés 

def roll():
    nb_dice = 4
    sum_dice = []
    nb_roll = 6

    for i in range(nb_roll):
        dice = [random.randint(1, 6) for x in range(nb_dice)]
        print(dice)
        dice.remove(min(dice))
        stat = sum(dice)
        print(stat)
        sum_dice.append(dice)
    print(sum_dice)

roll()