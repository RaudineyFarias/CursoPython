print("Valor Final da compra")

valor_compra = float(input("Qual o valor inicial da compra? "))

qtde_parcelas = int(input("Qual a Quantidade de parcelas? "))

if qtde_parcelas < 1 or qtde_parcelas >24:
    print("Opção Invalida!")
elif qtde_parcelas == 1:
    soma = valor_compra-(valor_compra*0.10)
    print(" ")
    print("Valor final da compra com desconto de 10%: ",soma)
else: 
    soma = (valor_compra*0.50)+valor_compra
    valor_parcelas = soma/qtde_parcelas
    print(" ")
    print("Valor inicial: ",valor_compra)
    print("Valor final da compra: "+"{:.2f}".format(soma))
    print("Quantidade de parcelas: ",qtde_parcelas)
    print("Valor de cada parcelas: ""{:.2f}".format(valor_parcelas))
