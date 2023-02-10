print("Seja Bem-vindo ao Restaurante de IFPB")

print(" ")

nome_garçom = input("Qual o nome do garçom? ")

n_mesa = int(input("Qual o número da mesa? "))

valor_inicial = float(input("Qual o Valor inicial? (Obs.:Sem os 10% do garçom): "))

qtde_integrantes = int(input("Qual a Quantidade de integrantes? "))

calculo = valor_inicial*0.10

valor_final = (valor_inicial*0.10)+valor_inicial

divisao = calculo/qtde_integrantes

print(" ")

print("Nome do Garçom: "+nome_garçom)

print("Mesa de Número: ",n_mesa)

print("Valor do Garçom: ",calculo)


print("Valor total com a despesa com os 10% do garçom: "+"{:.2f}".format(valor_final))

print("Valor que cada um irá pagar :"+"{:.2f}".format (divisao))