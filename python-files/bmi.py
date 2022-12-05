import math

sexo = str("h")#input("Homen(H) ou Mulher(M)?: " )
anos = int(19)#input("qual a sua idade?: ")
peso = float(76)#input("qual o seu peso(kl)?: ")
altura = int(172)#input("qual a sua altura(cm)?: ")
Pescoco = float(12.5)
Cintura = float(12.5)
Quadril = float(12.5)
num = float(((Quadril+Pescoco)-Cintura))
math.ceil(num)
print(num)
log1 = math.log((num,10))
log2 = math.log(altura,10)

if sexo == "h":
    #86.010 x log10 ( abdômen – pescoço ) – 70.041 x log10 ( altura ) + 36.76
    MASSA = ((86.010 * log1) - (97.684 * log2)) - 78.387
    print(MASSA)
else:
    #163.205 x log10 ( cintura + quadril – pescoço ) – 97.684 x log10 ( altura ) – 78.387
    print("ss")