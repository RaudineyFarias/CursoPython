def entrada():
 
  n1 = int(input("Qual o primeiro Numero? "))

  n2 = int(input("Qual o segundo Numero? "))

  n3 = int(input("Qual o ùltimo Numero? "))

  lista_num = [n1,n2,n3]

  return lista_num

def condicao(lista):

  return max(lista)
    

def exibir(resultado):
  
    print(resultado)