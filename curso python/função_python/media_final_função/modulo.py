from statistics import mean

def nome_alu():
    nome = input("Digite o seu nome: ")
  
    return nome

def notas():

    lista_notas = []

    for item in range(3):
        
        nota = int( input ( "Digite a nota: " ) )
       
        lista_notas.append(nota)
    
    return lista_notas
  

def media(lista):
  
  return mean(lista)

def conceito(nota):
  if nota >= 80:
    conc = "A"
  elif nota >= 50 and nota <=80:
    conc = "B"
  else:
    conc = "C"

  return conc

def Exibir(nome, media, conc, lista):
    print("Aluno(a) "+nome+" Seu conceito foi ["+conc+"] "+"As notas fornecidas foram:",lista," ficando com média final de: ", round(media,2))
  