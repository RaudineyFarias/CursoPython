print("Consumo de energia")

nome = input("Qual o seu nome? ")

cm = float(input("Qual o seu consumo desse mês? "))

if cm > 300:
    soma = cm*1.00
    print("Consumidor: "+nome)
    print("O seu consumo mensal foi de:",cm, "Kw/h")
    print("Preço do Kw/h R$ 1,00" + " | Total a pagar foi de: "+"{:.2f}".format (soma)+"R$")

elif cm >=200 and cm <300:
    soma = cm*0.80
    print("Consumidor: "+nome)
    print("O seu consumo mensal foi de:",cm, "Kw/h")
    print("Preço do Kw/h em R$ 0,80" + " | Total a pagar foi de: "+"{:.2f}".format (soma)+"R$")       
else:
    soma = cm*0.20
    print("Consumidor: "+nome)
    print("O seu consumo mensal foi de:",cm, "Kw/h")
    print("Preço do Kw/h R$ 0.20" + " | Total a pagar foi de: "+"{:.2f}".format (soma)+ "R$") 