print("Calculo de IR")

nome = input("Qual o Nome do funcionário? ")

SalBruto = float( input("Qual o Salário Bruto? "))

Inss = float( input("Qual o desconto do INSS? "))

Dep = int( input("Quantos dependentes? "))

Desconto = 90.00

BaseCal = SalBruto - (Desconto*Dep) - Inss


if BaseCal <= 900.80:
  Soma_ano = SalBruto*12
  print(nome)
  print("Isento de imposto de renda")
  print("Por Ano Você recebe ""{:.2f}". format(Soma_ano),"R$")
  print("O seu salário com os descontos é: ""{:.2f}". format(BaseCal),"R$")
elif BaseCal >900.80 and BaseCal<=1800.50:
  print(nome)
  Soma_ano = SalBruto*12
  IR = BaseCal*0.15-135.0
  print("Por Ano Você recebe ""{:.2f}". format(Soma_ano),"R$")
  print("O seu salário com os descontos é: ""{:.2f}". format(BaseCal),"R$")
  print("O seu imposto de renda será de: ""{:.2f}". format(IR),"R$")
else:
  BaseCal >1800.50
  Soma_ano = SalBruto*12
  IR = BaseCal*0.275-315.00
  print("Por Ano Você recebe "+"{:.2f}". format (Soma_ano),"R$")
  print("O seu salário com os descontos é: "+"{:.2f}". format(BaseCal),"R$")
  print("O seu imposto de renda será de: ""{:.2f}". format(IR),"R$")