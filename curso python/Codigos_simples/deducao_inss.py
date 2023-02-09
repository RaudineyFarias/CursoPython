Matricula = input ("Qual a matricula? ")

NomeFunc = input ("Qual o nome do Empregado? ")

SalarioBruto = float( input("Qual o salario bruto? "))

inss = (SalarioBruto*0.15)

salarioliquido = SalarioBruto-inss 

print (" ")

print ("Matricula de Nº:",Matricula,"|Nome: ",NomeFunc)

print (" ")

print ("Salário Bruto: ", SalarioBruto, "|INSS:", inss, "|Salario Liquido:", salarioliquido)