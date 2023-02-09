print("Tabuada mutiplicação!")
print("tipos de tabuadas ")
print("+ = Adição;")
print("- = Subtração;")
print("* = Multiplicação;")
print("/ = Divisão")
opcao = input("Digite o tipo de tabuada que você deseja: ")

while opcao!='0':
    if opcao == '+':
        num = int(input("Qual o numero deseja somar? "))
        n_soma = 0 
        while n_soma <=9:
            n_soma = n_soma+1
            print("{} + {} = {}".format(num,n_soma,(num+n_soma)))
    elif opcao =='*':
        num = int(input("Qual o numero deseja multiplicar? "))
        n_soma = 0 
        while n_soma <=9:
            n_soma = n_soma+1
            print("{} X {} = {}".format(num,n_soma,(num*n_soma)))
    elif opcao =='-':
        num = int(input("Qual o numero deseja subtrair? "))
        n_soma = 0 
        while n_soma <=9:
            n_soma = n_soma+1
            print("{} - {} = {}".format(num,n_soma,(num-n_soma)))
    elif opcao =='/':
        num = int(input("Qual o numero deseja dividir? "))
        n_soma = 0 
        while n_soma <=9:
            n_soma = n_soma+1
            print("{} / {} = {}".format(num,n_soma,(num/n_soma)))
            
    opcao = input("Digite outro tipo de tabuada ou digite [0] para sair: ")        
    if opcao =='0':
        print("fim do programa!")    