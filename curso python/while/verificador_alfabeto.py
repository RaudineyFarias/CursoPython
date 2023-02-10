print('Bem vindo ao programa de verificar  o alfabeto')

qtde_letra = int(input('Insira a quantidade de letras: '))

letra = input("Insira a Letra: ")

cont_vogal = 0

letra_maiusc = 0

letra_minusc = 0

while qtde_letra != '0' and letra != 'z' and letra != 'Z':

  if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    cont_vogal = cont_vogal + 1
  if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
    cont_vogal = cont_vogal + 1

  if letra.isupper():
    letra_maiusc = letra_maiusc + 1
  elif letra.islower():
    letra_minusc = letra_minusc + 1

  letra = input('Insira outra letra qualquer ou digite "z" para sair ')

if letra == 'z' or letra == 'Z':
  print('Quantidade de vogais: ', cont_vogal)
  print('Letras maisculas', letra_maiusc)
  print('Letras Minusculas:', letra_minusc)
