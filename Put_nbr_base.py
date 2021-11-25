
nb1 = 0
base = 0
div_res = 0
char = False
convert = ""

while str(nb1).isascii() and char == False :
    nb1 = input("Veuillez rentrer un chiffre à convertir : ")
    if bool(nb1.isnumeric()) == True :
        char = True
char = False
while str(base).isascii() and char == False :
    base = input("Veuillez rentrer une base pour la conversion : ")
    if bool(base.isnumeric()) == True and (int(base) >= 2 and int(base) <= 36) :
        char = True
nb1 = int(nb1)
base = int(base)
while nb1 >= 1 :
    div_res = nb1 % base
    if (div_res > 9) :
        div_res += 55
        convert += chr(div_res)
    else :
        convert += str(div_res)
    nb1 //= base
convert = convert [::-1]
print(convert)
