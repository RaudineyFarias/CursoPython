def qtde_maca():
  qtde = int(input("qual a quantidade de maçãs? "))

  return qtde
  
def calc_maca(qtde_maca):

  if qtde_maca >0 and qtde_maca <12: 
    soma = qtde_maca*1.50
  
  else:
    
    soma = qtde_maca*1.10
  
  return soma  
  
def exibir_result(valor):
  
  print("O Valor final é: {:.2f}".format(valor))
  