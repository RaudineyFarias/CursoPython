aluno =input ("qual o nome do Aluno? ")
nota1 =float (input("qual a primeira nota do aluno? "))
nota2 =float (input("qual a segunda nota do aluno? "))
nota3 =float (input("qual a segunda nota do aluno? "))

media = (nota1+nota2+nota3)/3

print ("A média do aluno ", aluno, "foi de ", media)
print ("A média do aluno " , aluno," foi de " +"{:.2f}".format (media))
