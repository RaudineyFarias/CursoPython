print("Nota Final ")

nome = input("Digite o nome do aluno: ")

n1 = float(input("Digite a primeira nota de aluno(a) " + nome + " : (ex.: 85.00) "))

n2 = float(input("Digite a segunda nota de aluno(a) " + nome + " : (ex.: 85.00) "))

n3 = float(input("Digite a terceira nota de aluno(a) " + nome + " : (ex.: 85.00) "))

media = (n1 + n2 + n3) / 3

if media < 49:
  print("Aluno(a) " + nome + ", Obteve o conceito D ")
  print("As notas Fornecidas foram Nota 1:",n1,"Nota 2:",n2," e Nota 3:",n3,"Com média final de: " +
        "{:.2f}".format(media))

elif media >= 50 and media <=69:
    print("Aluno(a) " + nome + ", Obteve o conceito C ")
    print("As notas Fornecidas foram Nota 1:",n1,"Nota 2:",n2," e Nota 3:",n3,"Com média final de: " +
          "{:.2f}".format(media))

elif media >= 70 and media <= 94:
    print("Aluno(a) " + nome + ", Obteve o conceito B ")
    print("As notas Fornecidas foram Nota 1:",n1,"Nota 2:",n2," e Nota 3:",n3,"Com média final de: " +
          "{:.2f}".format(media))

else:
    print("Aluno(a) " + nome + ", Obteve o conceito A")
    print("As notas Fornecidas foram Nota 1:",n1,"Nota 2:",n2," e Nota 3:",n3,"Com média final de: " +
          "{:.2f}".format(media))
