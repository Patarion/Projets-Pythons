LISTE = []
item = ""
choix = ""

while choix != "5" and bool(choix.isascii()) == True :
    print("_" * 50)
    print("Choisissez l'une de ses options suivantes : ")
    print("1: Ajouter un élément à la liste")
    print("2: Retirer un élément de la liste")
    print("3: Afficher la liste")
    print("4: Vider la liste")
    print("5: Quitter le programme")
    i = 0
    choix = input("Que voulez-vous faire? : ")
    if choix == "1" :
        item = input("Quel élément voulez-vous rajouter à votre liste de \
courses ? \n").capitalize()
        LISTE.append(item)
        print("L'élément suivant : " + item + " a été rajouté")
    elif choix == "2" :
        item = input("Quel élément voulez-vous retirer de la liste de \
course ? \n").capitalize()
        if item in LISTE:
            LISTE.remove(item)
            print("L'item suivant a ete supprime : " + item)
        else :
            print("Le choix que vous avez indiqué n'existe pas dans la liste.")
    elif choix == "3" :
        if LISTE :
            print("Voici votre liste d'épicerie")
            while LISTE[i::] :
                print(str(i + 1) + "." + LISTE[i])
                i += 1
    elif choix == "4" :
        if LISTE :
            LISTE.clear()
            print("La liste a ete supprime en entier")
        else :
            print("La liste est vide")

print("Thank you! Come again!")
