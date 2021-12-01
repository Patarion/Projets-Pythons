nombre1 = nombre2 = signe = ""
char = False

while str(nombre1).isascii() and not nombre1.isdigit() :
    nombre1 = input("Veuillez rentrer un premier chiffre : ")
while str(nombre2).isascii() and not nombre2.isdigit():
    nombre2 = input("Veuillez rentrer un deuxième chiffre : ")
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
