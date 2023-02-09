print ("Bem Vindo a Loja De Carros do Raud")

NomeCarro = input("Qual o modelo do carro? ")

ValorCarro = float(input ("Qual o valor de fábrica do carro "+ NomeCarro
+ "? "))

ValorFinal = (ValorCarro*10/100) + (ValorCarro*45/100) + ValorCarro

print("O valor final do carro ", NomeCarro, " " "{:.3f}".format (ValorFinal))
