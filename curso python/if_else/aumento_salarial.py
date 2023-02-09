print("Reajuste salarial")

nome = input("Qual o nome do funcionário? ")

salario = float( input("Qual o salario de "+nome+" ? "))

if salario <=1000.00:
    soma = (salario*0.30)+salario
    print(nome)
    print("salario anterior ",salario,"R$")
    print("O salario reajustado: ",soma,"R$")
elif (salario >1000.00 and salario <=1500.00):
    soma = (salario*0.20)+salario
    print(nome)
    print("salario anterior ",salario,"R$")
    print("O salario reajustado: ",soma,"R$")
elif (salario >1500.00 and salario <=2000.00):
    soma = (salario*0.15)+salario
    print(nome)
    print("salario anterior ",salario,"R$")
    print("O salario reajustadoe: ",soma,"R$")
elif (salario >2000.00 and salario<=2500.00):
    soma = (salario*0.10)+salario
    print(nome)
    print("salario anterior ",salario,"R$")
    print("O salario reajustado: ",soma,"R$")
else:
    salario>2500.00
    soma = (salario*0.05)+salario
    print(nome)
    print("salario anterior ",salario,"R$")
    print("O salario reajustado : ",soma,"R$")
