soma = 0
lista_números = [] # vazia

número = int(input("Digite o primeiro número (ex 45) ou 0 para sair: "))

while número != 0 :
    lista_números.append( número ) # inserir número no final
    soma = soma + número
    número = int(input("Digite outro número ou então 0 para sair: "))

print("A lista de números digitados abaixo:" )
print( lista_números )

print("Agora a soma final calculada é: ", soma )