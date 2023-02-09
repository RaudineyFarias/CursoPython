print('Idade das pessoas')

maior = 0

numero = 0

menor = 100

qtde_pessoas = int(input("insira a quantidade de pessoas: "))

while qtde_pessoas != 0:

  numero = numero + 1
  idade = int(input("Digite a idade da pessoa [" + str(numero) + "º]: "))
  qtde_pessoas = int(
    input(
      "Deseja digitar outra idade? Digite (1) para sim ou (-1) para não: "))
  if idade > maior:
    maior = idade

  if idade < menor:
    menor = idade

  if qtde_pessoas <= 0:
    media = (maior + menor) / numero
    print("A quantidade de pessoas: ", numero)
    print("A menor Idade: ", menor)
    print("A Maior Idade: ", maior)
    print("A idade média do grupo é: "+"{:.0f}".format(media))
    print('Fim do Programa !')
    break
else:
  menor = idade
  qtde_pessoas = qtde_pessoas + 1