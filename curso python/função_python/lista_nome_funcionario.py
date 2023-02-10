nome_fun = input('Digite o nome do funcionario ou "0" para sair: ')

while nome_fun != '0':

    clientes = ['caio', 'wellington', 'pedro', 'bruno', 'ana', 'caio', 'bruno', 'david', 'pedro']

    soma = clientes.count(nome_fun) ##Nesse passo ele vai procurar onde o nome digitado está e depois imprimir na tela


    remover = 0

    inserir = clientes.insert(0,nome_fun) #Esse passo o programa vai adicionar o nome do funcionario inserido na primeira posição

    count = clientes.count(nome_fun) #Nesse passo ele vai procurar onde o nome digitado está e depois imprimir na tela
    
    remover = clientes.remove(nome_fun)

    for i in clientes:
        if nome_fun == i:
          clientes.remove(nome_fun)
    
  
    print('Quantidade de vezes que aparece: ',soma)


    print('Lista depois dos processos: ',clientes)

    
    nome_fun = input('Digite outro nomo do funcionario ou "0" para sair: ')

if nome_fun == '0':
     print('Fim do programa! ')