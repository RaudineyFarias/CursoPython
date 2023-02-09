print("Classes de trabalhadores")

nome = input("Qual o nome do trabalhador? ")

sm = float( input("Qual o salario de "+nome+"? "))

Pecas_Fabric = int( input("Quantos pares foram produzidos por "+nome+"? "))

classeA = (sm*0.15)+sm
classeB = (sm*0.05)+sm


if (Pecas_Fabric<=30):
  print(" ")  
  print("O funcionario(a) "+nome)
  print("é pertencente a Classe C pois sua produção foi de", Pecas_Fabric, "Peças Fabricadas")
  print("Sendo assim receberá ",sm,"R$")
  
elif (Pecas_Fabric>30 and Pecas_Fabric<=44):
  print(" ")  
  print("O funcionario(a) "+nome)
  print("Salario minimo é: ",sm)  
  print("é pertencente a Classe B pois sua produção foi de", Pecas_Fabric, "Peças Fabricadas")
  print("Salario Final: ",classeB,"R$")
  
else:
  Pecas_Fabric>44
  print(" ")  
  print("O funcionario(a) "+nome)
  print("Salario minimo é: ",sm)  
  print("é pertencente a Classe A pois sua produção foi de", Pecas_Fabric, "Peças Fabricadas")
  print("Salario Final: ",classeA,"R$")