

#Definim les variables per a cada bitllet i per a cada moneda i una variable per als dinera a dividir.
diners=int(input("Indtrodueix una quantitat de diners: "))
b500=0
b200=0
b100=0
b50=0
b20=0
b10=0
b5=0
m2=0
m1=0
#Fiquem un bucle while per a cada bitllet i per a cada poneda, així cada vegada que no es pugui utilitzar més bitllets d'un tipus pasa al seguent.
while diners >= 500:
    diners-=500
    b500+=1
while diners >= 200:
    diners-=200
    b200+=1
while diners >= 100:
    diners-=100
    b100+=1
while diners >= 50:
    diners-=50
    b50+=1
while diners >= 20:
    diners-=20
    b20+=1
while diners >= 10:
    diners-=10
    b10+=1
while diners >= 5:
    diners-=5
    b5+=1
while diners >= 2:
    diners-=2
    m2+=1
while diners >= 1:
    diners-=1
    m1+=1
print("Bitllets 500:",b500,"Bitllets 200:",b200,"Bitllets 100:",b100,"Bitllets 50:",b50,"Bitllets 20:",b20,"Bitllets 10:",b10,"Bitllets 5:",b5,"Monedes 2:",m2,"Monedes 1:",m1)