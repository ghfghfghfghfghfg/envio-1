sexo = str("h")#input("Homen(H) ou Mulher(M)?: " )
anos = int(19)#input("qual a sua idade?: ")
peso = float(76)#input("qual o seu peso(kl)?: ")
altura = int(172)#input("qual a sua altura(cm)?: ")
gordura = float(12.5)#input("qual a sua quantidade de gordura corporal?: ")
niveis = ["Sedentário","Ativo leve","Ativo moderado","Muito ativo","Extremamente ativo"]
valor_niveis = [1.2,1.375,1.55,1.725,1.9]

if sexo == "h":
    BMR = float((13.397 * peso) + (4.799 *altura) - (5.677 * anos) + 88.362)
else:
    BMR = float((9.247 * peso) + (3.098*altura) - (4.330*anos) + 447.593)

print(BMR)

for x in range(5):
    print(niveis[x] + ":  %.2f" % + (valor_niveis[x]*BMR))
