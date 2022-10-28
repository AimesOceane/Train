#Algo tirer de CodeWars, Lance X dés 20 fait une moyenne puis dans une tranche de valeur comprise en 2 et 11 c'est Moyen, 11 et 20 c'est reussit
#et si c'est egal à 1 c'est un Echec Critique et egal à 20 c'est une reussite critique 

def lancer_des():
    import random
    lancer = int(input("Nombre de des lancer : ")) 
    des = []
    for i in range(lancer):
        de = random.randint(1, 20)
        des.append(de)
    somme = sum(des)
    moy_des = somme / lancer
    print(des, moy_des)

    for x in des:
        if x == 1:
            print("Echec Critique")
        if 2 < x < 11:
            print("Moyen")
        if 11 < x < 20:
            print("Reussite")
        if x == 20:
            print("Reussite Critique")
lancer_des()