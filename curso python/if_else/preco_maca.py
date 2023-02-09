print("Seja bem vindo ")

qtd_maca = int( input("qual a quantidade de maçãs você vai querer? "))

maca=1.50

if (qtd_maca >0 and qtd_maca <12): 
  soma = qtd_maca*1.50
  
else:
  qtd_maca >=12
  soma = qtd_maca*1.10
  
print("o valor a ser pago é: "+"{:.2f}".format(soma))
print("obrigado pela preferencia!!")