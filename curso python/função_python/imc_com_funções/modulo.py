def peso():

  peso = float(input("Qual o seu peso? "))

  return peso


def altura():

  altura = float(input("Qual a sua altura? "))

  return altura


def calculo(peso, altura):

  imc = (peso / (altura * altura))*10000


  return imc
  
def condicao(valor):
    
  if (valor <18.5):
    imc =   "O seu IMC é: "+"{:.2f}".format (valor)+" Você está abaixo do seu peso ideal"
  elif (valor >=18.5 and valor<=24.9):
    imc = "O seu IMC é: "+"{:.2f}".format (valor)+" Parabéns! Você está no seu peso ideal!"
  elif (valor>=25.0 and valor<=29.9): 
    imc =   "O seu IMC é: "+"{:.2f}".format (valor)+" Você está acima do seu peso (sobrepeso)"
  elif (valor >=30.0 and valor<=34.9):
    imc ="O seu IMC é: "+"{:.2f}".format (valor)+" Obesidade grau I"
  elif (valor >=35.0 and valor <=39.9):
    imc ="O seu IMC é: "+"{:.2f}".format (valor)+" Obesidade grau II"    
  else:
    imc ="O seu IMC é: "+"{:.2f}".format (valor)+" Obsesidade grau III" 

  return imc
    
def exibir(result):

    print(result)