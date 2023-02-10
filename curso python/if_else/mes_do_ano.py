print("Digite um numero que eu digo qual o mês ele se refere")
print("  ")

num_mes = int(input("Digite um numero: "))

if (num_mes <1 or num_mes >12):
    print("Resposta Invalida")

elif num_mes ==1:
    print("Mês janeiro")

elif num_mes ==2:
    print("Mês Fevereiro")

elif num_mes ==3:
    print("Mês Março")

elif num_mes ==4:
    print("Mês Abril")

elif num_mes ==5:
    print("Mês Maio")

elif num_mes ==6:
    print("Mês Junho")

elif num_mes ==7:
    print("Mês julho")

elif num_mes ==8:
    print("Mês Agosto")

elif num_mes ==9:
    print("Mês Setembro")

elif num_mes ==10:
    print("Mês Outubro")

elif num_mes ==11:
    print("Mês Novembro")
    
else:
    print("Mês Dezembro")        