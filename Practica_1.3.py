

password=input("Introduce un password (debe tener una longitud entre 6 y 16, y debe contener al menos una minúscula, una mayúscula, una cifra y un '$','#' o '@'):")
#Definim el bulcle while per a que repeteixi la validació fins que la password ingresada sigui correcta.
valida = False
while valida == False:
# Defineixo les variables com a falses, per a partir que es van complint canviar-les a True
    largo = False
    mayus = False
    minus = False
    num = False
    sym = False
    c=0
#Introduím un for per a poder validar la llargada.
    for letra in password:
        c += 1
    if c >= 6 and c <= 10:
        largo = True
#Afegim un segon for per a poder validar les altres condicions.
    for letra in password:
        if letra>="A" and letra <="Z":
            mayus=True
        elif letra>="a" and letra <="z":
            minus=True
        elif letra>="0" and letra<="9":
            num=True
        elif letra>="$" and letra<="@":
            sym=True
#Seguidament validem si la password ingresada es vàlida
    if largo==True and mayus==True and minus==True and num==True and sym==True:
        valida=True
#A continuació si la password es valida, se li va indicant al usuari amb un ordre.
    if largo==False:
        print("El password tiene {} caracteres y debe tener entre 6 y 10".format(c))
    else:
        if mayus==False:
            print("El password debería contener al menos una mayúscula")
        else:
            if minus==False:
                print("El password debería contener al menos una minúscula")
            else:
                if num==False:
                    print("El password debería contener al menos una cifra")
                else:
                    if sym==False:
                        print("El password debería contener al menos un '$','#','@'")
#Finalment si la password ingresada no és valida, es torna a demanar. En cas de que sigui correcta s'acaba el bucle.
    if valida==False:
        password=input("Introduce un nuevo passwor: ")
print("Password Correcto")