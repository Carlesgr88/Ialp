
#Importem la llibreria random per a aconseguir el número aleatori.
import random
intents=0

num_adv=random.randint(0,21)
#Fiquem un bucle while per a poder controlar els intents límit.
while intents <=2:
    intents+=1
    num = int(input("Dis un número:(0-20) "))
#Afegim un if per a poder indicar al usuari si el número que a ficat és més gran o més petit que el número a endivinar
    if num!=num_adv:
        if num> num_adv:
            print("El número és més gran que el número a adivinar")
        elif num< num_adv:
            print("El número és més petit que el número a adivinar ")
    print("Intents restants: ",3-intents)
#Amb aquest if final indiquem si l'usuari a endivinat el nombre o no.
if num== num_adv:
    print("Felicitats has endivinat el número!! :)")
else:
    print("vaya parguela")