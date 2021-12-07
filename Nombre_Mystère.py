from random import randint

MYS = randint(0, 50)
nb_essaies = 5
rep = ""

print("Bienvenue au jeu du nombre mystère")
while bool(rep.isascii()) and nb_essaies > 0  and rep != str(MYS) :
    print("Il vous reste " + str(nb_essaies) + " essaies")
    rep = input("Veuillez rentrer un nombre je vous pris : \n")
    if bool(rep.isdigit()) == False or (int(rep) > 50) or int(rep) < 0 :
        print("Veuillez rentrer un nombre enetre 0 et 50!")
    elif int(rep) > MYS :
        print("Votre nombre est plus grand que celui recherché")
        nb_essaies -= 1
    elif int(rep) < MYS :
        print("Votre nombre est plus petit que celui recherché")
        nb_essaies -= 1
    else :
        print("Vous avez gagné! Ils vous restaient " + str(nb_essaies) + " essaies")
if nb_essaies == 0 :
    print ("Meilleur chance la prochaine fois!")
