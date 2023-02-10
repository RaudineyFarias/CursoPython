print('Bem vindo ao programa de eleição de canais')
print('Neste Programa você escolherá os Canais abaixo para votar:')
print('Canal 5, Canal 7, Canal 10, Canal 12')
print('Para cada canal votar em seu respectivo número! ')
print('Ex.: Canal 7 deve se votar "7" ')

qtde_votos = int(input('Insira a quantidade de votos: '))

c = 0

voto = 0

canal_5 = 0

canal_7 = 0

canal_10 = 0

canal_12 = 0

while qtde_votos != 0:

  if qtde_votos < 0:
    print('Quantidade invalida')
    qtde_votos = int(
      input('digite [ 1 ] para votar novamente ou [ 0 ] para sair: '))
    if qtde_votos == 0:
      print('Programa encerrado!')
      break

  c = c + 1

  voto = int(input('Insira o [ ' + str(c) + 'º] voto: '))

  if voto != 5 and voto != 7 and voto != 10 and voto != 12:
    print('Voto invalido!')
    qtde_votos = int(
      input('digite [ 1 ] para continuar votando ou [ 0 ] para sair: '))

  if voto == 5:
    canal_5 = canal_5 + 1
  elif voto == 7:
    canal_7 = canal_7 + 1
  elif voto == 10:
    canal_10 = canal_10 + 1
  elif voto == 12:
    canal_12 = canal_12 + 1
  qtde_votos = int(
    input('digite [ 1 ] para votar novamente ou [ 0 ] para sair: '))

  if qtde_votos == 0:
    if canal_5 > canal_7 and canal_5 > canal_10 and canal_5 > canal_12:
      porcent = c / canal_5
      print("Porcentagem de votos:" + '{:.2f}'.format(porcent))
      print('Quantidade de votos: ', c)
      print('O canal vencedor foi o canal 5, com ', canal_5, ' votos válidos!')
      print('Canal 7: ', canal_7)
      print('Canal 10:', canal_10)
      print('Canal 12:', canal_12)
      print('Programa encerrado!')
    elif canal_7 > canal_5 and canal_7 > canal_10 and canal_7 > canal_12:
      porcent = c / canal_7
      print("Porcentagem de votos:" + '{:.2f}'.format(porcent))
      print('Quantidade de votos: ', c)
      print('O canal vencedor foi o canal 7, com ', canal_7, ' votos válidos!')
      print('Canal 5: ', canal_5)
      print('Canal 10:', canal_10)
      print('Canal 12:', canal_12)
      print('Programa encerrado!')
    elif canal_10 > canal_5 and canal_10 > canal_7 and canal_10 > canal_12:
      porcent = c / canal_10
      print("Porcentagem de votos:" + '{:.2f}'.format(porcent))
      print('Quantidade de votos: ', c)
      print('O canal vencedor foi o canal 10, com ', canal_10,
            ' votos válidos!')
      print('Canal 5: ', canal_5)
      print('Canal 7:', canal_7)
      print('Canal 12:', canal_12)
      print('Programa encerrado!')
    elif canal_12 > canal_5 and canal_12 > canal_7 and canal_12 > canal_10:
      porcent = c / canal_12
      print("Porcentagem de votos:" + '{:.2f}'.format(porcent))
      print('Quantidade de votos: ', c)
      print('O canal vencedor foi o canal 12, com ', canal_12,
            ' votos válidos!')
      print('Canal 5: ', canal_5)
      print('Canal 7: ', canal_7)
      print('Canal 10:', canal_10)
      print('Programa encerrado!')
