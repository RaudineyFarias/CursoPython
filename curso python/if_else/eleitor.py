nome = input("Qual o seu nome? ")
idade = int( input("Qual a sua idade? "))

if (idade < 16):
  print(nome+" não eleitor!")
elif (idade >= 18 and idade <=65):
  print(nome+" Eleitor obrigatório!")
else:
  (idade ==16 and idade ==17) or (idade >65)
  print(nome+" Eleitor facultativo!")  