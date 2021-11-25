nombre1 = 0
nombre2 = 0
signe = ""
char = False

while str(nombre1).isascii() and char == False :
    nombre1 = input("Veuillez rentrer un premier chiffre : ")
    if bool(nombre1.isnumeric()) == True :
        char = True
char = False
while str(nombre2).isascii() and char == False :
    nombre2 = input("Veuillez rentrer un deuxième chiffre : ")
    if bool(nombre2.isnumeric()) == True :
        char = True
char = False
while char == False :
    signe = input("Veuillez rentrer l'opérateur de l'équation : ")
    if signe == '+' or signe == '-' or signe == '*' or signe == '/':
        char = True
if signe == '+' :
    print("Le résultat de l'addition de " + nombre1 + " et de " + nombre2
            + " est de " + str(int(nombre1) + int(nombre2)))
elif signe == '-' :
    print("Le résultat de la soustraction de " + nombre1 + " et de " + nombre2
            + " est de " + str(int(nombre1) - int(nombre2)))
elif signe == '*' :
    print("Le résultat de la multiplication de " + nombre1 + " et de "
            + nombre2 + " est de " + str(int(nombre1) * int(nombre2)))
elif signe == '/' :
    print("Le résultat de la division de " + nombre1 + " et de " + nombre2
            + " est de " + str(int(nombre1) // int(nombre2)))
