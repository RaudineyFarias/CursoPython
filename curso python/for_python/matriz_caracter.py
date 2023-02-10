
caracter = input("Digite o caracter: ")

linha = int(input("Digite a quantidade de linhas: "))

coluna = int(input("Digite a quantidade de colunas: "))

for  l in range(0,linha):
    for c in range(0,coluna):
        print('{:2}'.format(caracter), end='')
    print()   