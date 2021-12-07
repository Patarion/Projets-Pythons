from random import randint

CHOIX = ""
nb_potions = 3
pv_player = 50
pv_monster = 50
random = 0
########################################################################
def ft_potion(nb_potions) :
    global pv_player, random
    if nb_potions > 0 :
        random = randint(15,50)
        pv_player += random
        if pv_player > 50 :
            pv_player = 50
        nb_potions -= 1
        print("Vous avez récupérer " + str(random) + " PV et vous êtes \
 rendu à " + str(pv_player) + "PV")
        print("Pendant que vous buviez, le monstre vous attaque...")
        random = randint(10,15)
        pv_player -= random
        print("Le monstre vous a fait " + str(random) + " et il vous reste\
 " + str(pv_player))
        return nb_potions
    else :
        print("Vous n'avez plus de potions... Attaquez bon sang!")
        return 0
    
#######################################################################
def ft_attaque() :
    global pv_player, pv_monster, random
    print("Vous tentez d'infligé des dégats à votre adversaire")
    random = randint(5,15)
    pv_monster -= random
    print("Votre arme a fait " + str(random) + " degats et il reste\
 " + str(pv_monster) + " à votre adversaire")
    if pv_monster > 0 :
        print("Le monstre tente de vous attaquer et...")
        random = randint(10,15)
        pv_player -= random
        if pv_player > 0 :
            print("Le monstre vous a fait " + str(random) + " degats et il vous\
 reste " + str(pv_player) + " PV")
        else :
            return

############################################################################
def combat() :
    global CHOIX, nb_potions, pv_player, pv_monster, random
    print("Vous avez décidé de vous battre on dirait\n")
    while bool(CHOIX.isascii()) == True :
        if pv_player <= 0 or pv_monster <= 0 :
            break
        CHOIX = input("Que voulez faire? (1).Attaquer (2).Boire une Potion \n")
        if CHOIX == "1" :
            ft_attaque()
        elif CHOIX == "2" :
            nb_potions = ft_potion(nb_potions)
        else :
            print("Mais voyons êtes-vous capable de choisir entre 2 options?!")
            
############################################################################
print("Un ennemi vous barre la route. Voulez vous vous battre ou fuire ?")
while bool(CHOIX.isascii()) == True :
    CHOIX = input("(1). Se Battre (2). Fuir\n")
    if CHOIX == "1" :
        print("Au combat!")
        combat()
        break
    elif CHOIX == "2" :
        print("Fuck this shit I'm out")
        break
if pv_monster <= 0 :
    print("Vouz vivez pour mourir un autre jour")
elif pv_player <= 0 :
    print("Vous êtes morts")
else :
    print("Issu du combat inconnu")
