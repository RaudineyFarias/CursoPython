
def nome():
  name = input("Qual o seu nome? ")

  return name

def idade():
    id = int( input("Qual a sua idade? "))

    return id

def condicao(idade):
  
  if (idade < 16):
     msg =", Não eleitor!"  
  elif (idade >= 18 and idade <=65):
     msg=", Eleitor obrigatório!"
  else:
    (idade ==16 and idade ==17) or (idade >65)
    msg =", Eleitor facultativo!"
    
  return msg  

def exibir(nome,mensagem):
  
  print(nome,mensagem)