print ("Bem Vindo ao PRS (Programa De Reajuste De Salário)")

NomeFunc = input("Qual o nome do funcionário?  ")

salario = float (input("Qual o salário do "+ NomeFunc + " "))

resultado = (salario*20/100)+salario

print ("O valor do salário ", NomeFunc, " ""{:.2f}".format (resultado))


# vinte porcento = 20 / 100 = 0.20