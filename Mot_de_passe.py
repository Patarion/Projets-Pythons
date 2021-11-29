COURT = "votre mot de passe est trop court"

mdp = ""
term = False

while bool(mdp.isascii()) == True and term == False :
    mdp = input("Veuillez rentrer un mot de passe (8 caractères min) : ")
    if mdp == "" :
        print(COURT.upper())
    elif len(mdp) >= 8 and bool(mdp.isdigit()) == False :
        print("Inscription terminée")
        term = True
    elif bool(mdp.isdigit()) == True :
        print("Le mot de passe ne contient que des chiffres")
    else :
        print(COURT.capitalize())
