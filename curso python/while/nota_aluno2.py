print("Seja bem vindo ao programa de notas")

nome = input("Qual o seu nome? ")

qtde_notas = int(input("Insire o conjunto de notas que você deseja: "))



nota = 0 

while qtde_notas!= 0:
  nota = float(input(nome+"Qual a Sua Nota? "))
  qtde_notas = int(input("Deseja inserir outra nota? Digite (1) para sim ou (0) Não: "))
  if qtde_notas == 0:
    print("Nome: "+nome)
    print(nota)
  else:
    qtde_notas =qtde_notas+1