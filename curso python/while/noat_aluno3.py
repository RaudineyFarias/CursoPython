print("Seja bem vindo ao programa de notas")

maior = 0

nome = input("Qual o seu nome? ")

qtde_notas = int(input("Qual a quantidade de notas: "))


while qtde_notas!= 0:
  
  nota = float(input(nome+" Qual a Sua Nota? "))
  qtde_notas = int(input("Deseja inserir outra nota? Digite (1) para sim ou (0) Não: "))
  if nota > maior:
    maior = nota
if qtde_notas == 0:
  print("Nome: "+nome)
  print("Sua última Nota foi: ",nota)
  print("Sua maior Nota é: ",maior)  
        
else:
    qtde_notas = qtde_notas+1