num = int(input('Digite um numero: '))

lista_num = []

c = 0

while num != -1:
    lista_num.append(num)
    if num <0:
        lista_num.pop()  
    num = int(input('Digite outro numero ou digite "-1" para sair: '))
    
    



print(sorted(lista_num))