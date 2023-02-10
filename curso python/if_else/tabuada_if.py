print('programa de tabuada adição e mutiplicação')

print("Digite qual o tipo de tabuada que você deseja! ")

tipo_tab = input("Para adição digite '+'  ou '*' para mutiplicação :")

if tipo_tab != '*' and tipo_tab !='+' and tipo_tab!='0':
    print("Opção Invalida!")
    tipo_tab = input("Digite '+' para adição , '*' para mutiplicação ou '0' para sair:") 

while tipo_tab == '*' or tipo_tab =='+':    
    if tipo_tab == '*':
        numero = int(input('Digite um numero para ver sua tabuada: '))
        print('-'*12)
        print('{}x{} = {}'. format(numero, 1, numero*1))
        print('{}x{} = {}'. format(numero, 2, numero*2))
        print('{}x{} = {}'. format(numero, 3, numero*3))
        print('{}x{} = {}'. format(numero, 4, numero*4))
        print('{}x{} = {}'. format(numero, 5, numero*5))
        print('{}x{} = {}'. format(numero, 6, numero*6))
        print('{}x{} = {}'. format(numero, 7, numero*7))
        print('{}x{} = {}'. format(numero, 8, numero*8))
        print('{}x{} = {}'. format(numero, 9, numero*9))
        print('{}x{} = {}'. format(numero, 10, numero*10))
        print('-'*12)

        tipo_tab = input("Se calcular mais um vez digite '+' para adição , '*' para mutiplicação ou '0' para sair:") 

    if tipo_tab == '+':
        numero = int(input('Digite um numero para ver sua tabuada: '))
        print('-'*12)
        print('{}+{} = {}'. format(numero, 1, numero+1))
        print('{}+{} = {}'. format(numero, 2, numero+2))
        print('{}+{} = {}'. format(numero, 3, numero+3))
        print('{}+{} = {}'. format(numero, 4, numero+4))
        print('{}+{} = {}'. format(numero, 5, numero+5))
        print('{}+{} = {}'. format(numero, 6, numero+6))
        print('{}+{} = {}'. format(numero, 7, numero+7))
        print('{}+{} = {}'. format(numero, 8, numero+8))
        print('{}+{} = {}'. format(numero, 9, numero+9))
        print('{}+{} = {}'. format(numero, 10, numero+10))
        print('-'*12) 
        tipo_tab = input("Se calcular mais um vez digite '+' para adição , '*' para mutiplicação ou '0' para sair:")

    if tipo_tab != '*' and tipo_tab !='+' and tipo_tab!='0':
        print("Opção Invalida!")
        tipo_tab = input("Digite '+' para adição , '*' para mutiplicação ou '0' para sair:")    

    if tipo_tab == '0':
        print('Programa encerrado!')
        break    