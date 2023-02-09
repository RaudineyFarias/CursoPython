print("Digite três Numero e veja qual é o maior")

n1 = int(input("Qual o primeiro Numero? "))

n2 = int(input("Qual o segundo Numero? "))

n3 = int(input("Qual o ùltimo Numero? "))

if n1 > n2 and n1 > n3:
    print("O Numero ",n1,"É o Maior Numero")
elif n2> n1 and n2 >n3:
    print("O Numero ",n2,"É o Maior Numero")
else:
    print("O Numero ",n3,"É o Maior Numero")