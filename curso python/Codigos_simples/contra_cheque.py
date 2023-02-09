nome = input("Qual o nome do funcionário? ")

sal_bruto = float(input("Qual o salario bruto? "))

sind = sal_bruto*0.05

IR = sal_bruto*0.11

inss = sal_bruto*0.08

sal_liq = sal_bruto-(IR+inss+sind)

print("       ")

print("Nome: ",nome)

print("O salário Bruto é: ",sal_bruto)

print("Descontos-> ""IR: "+"{:.2f}".format(IR),"|INSS: "+"{:.2f}".format (inss),"|Sindicato: "+"{:.2f}".format(sind))

print("Salário Liquido: ", sal_liq)