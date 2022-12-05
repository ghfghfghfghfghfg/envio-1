 
gordura_corporal = float(input("Digite sua porcentagem de gordura: "))
peso = float(input("Digite seu peso em Kg: "))
altura = float(input("Digite sua altura (cm): "))
 
Gordura_corporal_total = (peso * ( gordura_corporal/ 100 ))
Peso_magro = (peso * (1-( gordura_corporal/ 100 )))

pes = 0.0328084
polegada=  0.393701

FFMI = ( Peso_magro / 2.2 ) * 2.20462 / ((altura/100)**2)
FMI_ajustado = (FFMI + (6.1 * (1.8- (altura/100)) ))

print("Massa sem gordura: " + str(Peso_magro))
print("Gordura corporal: " + str(Gordura_corporal_total))
print("FFMI: " + str(FFMI))
print("FMI normalizado: " + str(FMI_ajustado))