numero = int(input('Digite um numero: '))

lista_num = []

while numero != 0:
    lista_num.append(numero)
    numero = int(input('Digite um numero: '))

if numero ==0:
    print(lista_num)
    print('O maior número é o: ',max(lista_num))
    num_opcao = int(input('digite um numero dos que foram inseridos e direi a posição em que ele se encontra: '))
    print(lista_num.index(num_opcao))
    print(' ')
    print('Fim do programa!')