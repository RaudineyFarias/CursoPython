numero = int(input("Digite um numero ou '0' para Sair: "))

lista_num = []

num_pares = []

num_imp = []


c = 0

i = 0

while numero != 0:
    lista_num.append(numero)
    
    if numero % 2 == 0:
        num_pares.append(numero)
        c = c+1    
    else:
        num_imp.append(numero)
        i = i + 1
    numero = int(input("Digite outro numero ou '0' para Sair: "))    

    

if numero == 0:
    print(' ')
    print('Numeros digitados: ',lista_num)
    print('Quantidade de números pares:  '+str(c))
    print('Numeros Pares inseridos: ',num_pares)
    print('Quantidade de números Impares: '+str(i))
    print('Numeros Impares inseridos: ',num_imp)
    