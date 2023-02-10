num_in = int(input("Digite o primeiro numero ou digite '0' para sair: "))

lista_num = []

c = 0

while num_in != 0:
  lista_num.append(num_in)
  c = c + num_in
  num_in = int(input("digite outro numero: "))
  


print('A lista de numeros que você digitou:')
print(lista_num)

print('A soma dos numeros digitados é: ', c)