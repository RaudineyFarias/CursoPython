print ("IFPB")

Nota1 = float( input ("Qual a primeira Nota do aluno? "))

Nota2 = float( input ("Qual a segunda Nota do aluno? "))

Nota3 = float( input ("Qual a última Nota do aluno? "))

porcent1 = Nota1*20/100
porcent2 = Nota2*30/100
porcent3 = Nota3*50/100

media = porcent1+porcent2+porcent3

print("O valor final da média do aluno é:  "+ "{:.1f}".format (media))